#!/usr/bin/env python
# coding: utf-8

# # Network training
# 
# For our project, we constructed a Vision Transformer (ViT) instance that we named `GlowDeTR` to assess how light exposure affects Neural Network's result at classification.


import torch
import json
import ast
import torch.nn as nn
import numpy as np
import albumentations
from math import floor
from tqdm import tqdm

from pathlib import Path
from PIL import Image, ImageDraw
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from transformers import YolosForObjectDetection, AutoModelForObjectDetection, AutoImageProcessor, TrainingArguments, Trainer
from datasets import load_dataset, Dataset, concatenate_datasets
from tenacity import retry, wait_fixed, stop_after_attempt



# leopard photos
wildlife_ds = load_dataset("SeaSponge/wildme_dataset", cache_dir=Path.cwd() / "yalu_dataset")


class GlowYolos(YolosForObjectDetection):
    def forward(self, pixel_values, labels=None, **kwargs):
        outputs = super().forward(pixel_values=pixel_values, **kwargs)
        loss = None
        
        if labels is not None:
            # Use the `common_step` to calculate loss
            loss = self.common_step(labels, outputs.logits, outputs.pred_boxes)
        
        return {"loss": loss, **outputs}


tensor2PIL = transforms.ToPILImage()

transform1 = albumentations.Compose(
    [
        # albumentations.HorizontalFlip(p=1.0),
        albumentations.HorizontalFlip(p=0.5),
        albumentations.LongestMaxSize(max_size=600),
        albumentations.RandomBrightnessContrast(p=0.5),
    ],
    bbox_params=albumentations.BboxParams(format="coco", label_fields=["category"]),
)

# checkpoint = "facebook/detr-resnet-50"
device = "cuda" if torch.cuda.is_available else "cpu"


wildlife_ds


# Two labels: leopard & hyenas
try:
    print(wildlife_ds["train"])    
    wildlife_train_ds = wildlife_ds["train"]
    wildlife_val_ds = wildlife_ds["validation"]
except Exception as e:
    print(f"Errored due to -> {e}")
    wildlife_train_ds = wildlife_ds
    del wildlife_ds

def draw_image_from_idx(dataset, idx):
    sample = dataset[idx]
    image = sample["image"]
    annotations = sample["objects"]
    draw = ImageDraw.Draw(image)
    width, height = sample["width"], sample["height"]

    for i in range(len(annotations["bbox"])):
        box = annotations["bbox"][i]
        class_idx = annotations["label"][i]
        x, y, w, h = tuple(box)
        if max(box) > 1.0:
            x1, y1 = int(x), int(y)
            x2, y2 = int(x + w), int(y + h)
        else:
            x1 = int(x * width)
            y1 = int(y * height)
            x2 = int((x + w) * width)
            y2 = int((y + h) * height)
        print(f"height -> {height} | width -> {width}")
        print(f"x1 -> {x1} | y1 -> {y1} | x2 -> {x2} | y2 -> {y2}")
        draw.rectangle((x1, y1, x2, y2), outline="red", width=6)
        draw.text((x1, y1), annotations["label"], fill="white", font_size=40)
    return image


draw_image_from_idx(dataset=wildlife_train_ds, idx=200)

import matplotlib.pyplot as plt

def plot_images(dataset, indices):
    """
    Plot images and their annotations.
    """
    num_rows = len(indices) // 3
    num_cols = 3
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))

    for i, idx in enumerate(indices):
        row = i // num_cols
        col = i % num_cols

        # Draw image
        image = draw_image_from_idx(dataset, idx)

        # Display image on the corresponding subplot
        axes[row, col].imshow(image)
        axes[row, col].axis("off")

    plt.tight_layout()
    plt.show()


# Now use the function to plot images

plot_images(wildlife_train_ds, range(9))

def formatted_anns(image_id, category, area, bbox):
    annotations = []
    for i in range(0, len(category)):
        new_ann = {
            "image_id": image_id,
            "category_id": category[i],
            "isCrowd": 0,
            "area": area[i],
            "bbox": list(bbox[i]),
        }
        annotations.append(new_ann)

    return annotations


image_processor = AutoImageProcessor.from_pretrained("hustvl/yolos-small")


# transforming a batch

def transform_aug_ann(examples):
    image_ids = examples["image_id"]
    images, bboxes, area, categories = [], [], [], []
    for image, objects in zip(examples["image"], examples["objects"]):
        image = np.array(image.convert("RGB"))[:, :, ::-1]
        #! category needs to be list, hence I put the extra brackets around it
        out = transform1(image=image, bboxes=objects["bbox"], category=objects["category"])

        area.append(objects["area"])
        images.append(out["image"])
        bboxes.append(out["bboxes"])
        categories.append(out["category"])

    targets = [
        {"image_id": id_, "annotations": formatted_anns(id_, cat_, ar_, box_)}
        for id_, cat_, ar_, box_ in zip(image_ids, categories, area, bboxes)
    ]

    return image_processor(images=images, annotations=targets, return_tensors="pt")

wildlife_train_ds_transformed = wildlife_train_ds.with_transform(transform_aug_ann)
wildlife_val_ds_transformed = wildlife_val_ds.with_transform(transform_aug_ann)


print(f"wildlife_train_ds_transformed -> {wildlife_train_ds_transformed}")
del wildlife_train_ds
del wildlife_val_ds


label2id = {"leopard" : 0, "hyena": 1}
id2label = {v:k for k, v in label2id.items()}

def collate_fn(batch):
    pixel_values = [item["pixel_values"] for item in batch]
    encoding = image_processor.pad(pixel_values, return_tensors="pt")
    labels = [item["labels"] for item in batch]
    batch = {}
    batch["pixel_values"] = encoding["pixel_values"]
    batch["pixel_mask"] = encoding["pixel_mask"]
    batch["labels"] = labels
    return batch

def collate_fn_yolo(batch):
    pixel_values = [item["pixel_values"] for item in batch]
    encoding = image_processor.pad(pixel_values, return_tensors="pt")
    labels = [item["labels"] for item in batch]
    batch = {}
    batch['pixel_values'] = encoding['pixel_values']
    batch['labels'] = labels
    return batch


# Define the training arguments

#! Too large
# checkpoint = "SenseTime/deformable-detr"

checkpoint = "hustvl/yolos-small"

model = YolosForObjectDetection.from_pretrained(checkpoint,
                                                id2label=id2label,
                                                label2id=label2id,
                                                ignore_mismatched_sizes=True)

image_processor = AutoImageProcessor.from_pretrained(checkpoint)

#! From physical testing, batchsz=4 seems to be fine | 6364MiB / 11264MiB
#! update, I suppose batchsz=6 also works now. | 8534MiB / 11264MiB
#! batchsz=6 is cutting it very fine on my machine, want more redundancy

# max_steps=3000 takes ~ 20 hours

training_args = TrainingArguments(
    output_dir="glow-model",
    per_device_train_batch_size=5,
    max_steps=200,
    fp16=True,
    save_steps=10,
    logging_steps=30,
    learning_rate=1e-5,
    weight_decay=1e-4,
    save_total_limit=2,
    remove_unused_columns=False,
    push_to_hub=True,
    lr_scheduler_type="cosine_with_restarts",  # Cosine scheduler with restarts
)


# Define the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=collate_fn_yolo,
    train_dataset=wildlife_train_ds_transformed,
    eval_dataset=wildlife_val_ds_transformed,
    tokenizer=image_processor,
)

trainer.train()
# saved_path = Path.cwd() / "results"
# trainer.save_model(saved_path)

