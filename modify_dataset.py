import torch
import ast
import numpy as np
from tqdm import tqdm

from pathlib import Path
from PIL import Image, ImageDraw
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from transformers import AutoImageProcessor, TrainingArguments, Trainer, YolosForObjectDetection
from datasets import load_dataset, Dataset, DatasetDict


device = "cuda" if torch.cuda.is_available else "cpu"

num_shards = 4
# ! I've already finished uploading the first 10%, so just handling the remaining 90%

wildlife_ds = load_dataset("yin30lei/wildlife-from-wildme", split=f"train[10%:50%]", cache_dir=Path.cwd() / "wildlife", num_proc=2)
train_test_split = wildlife_ds.train_test_split(test_size=0.3, seed=42)
wildlife_train_ds = train_test_split["train"]
val_test_split = train_test_split["test"].train_test_split(test_size=0.4, seed=5)

wildlife_val_ds = val_test_split["train"]
wildlife_test_ds = val_test_split["test"]

del wildlife_ds
del train_test_split
del val_test_split

print(wildlife_train_ds)
print(wildlife_val_ds)
print(wildlife_test_ds)

# raise SystemExit("checking")
print(wildlife_val_ds[10])

def update_record(record, idx):
    width, height = record["image"].size  # Assuming "image" is a PIL Image
    record["image_id"] = idx
    record["width"] = width
    record["height"] = height

    # Parse and update "bbox"
    box = record["bbox"]
    record["objects"] = {}
    record["objects"]["label"] = record["label"]
    bbox_list = ast.literal_eval(box)
    record["objects"]["bbox"] = []
    for ent in bbox_list:
        x1, y1, x2, y2 = ent
        
        x1 /= width
        y1 /= height
        x2 /= width
        y2 /= height

        # Clamp values to ensure within [0, 1]
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(1, x2), min(1, y2)

        # Append the normalized and clamped bbox
        record["objects"]["bbox"].append([x1, y1, x2, y2])
    
    record["objects"]["area"] = []
    for entry in bbox_list:
        w = entry[2]
        h = entry[3]
        record["objects"]["area"].append(abs(w) * abs(h))
    
    record["objects"]["category"] = [record["category"] for _ in range(len(bbox_list))]
    
    record.pop("category", None)
    record.pop("bbox", None)
    record.pop("label", None)
    return record



# # Use the map function to apply the update
wildlife_train_ds = wildlife_train_ds.map(
    lambda record, idx: update_record(record, idx),
    with_indices=True,
)



wildlife_val_ds = wildlife_val_ds.map(
    lambda record, idx: update_record(record, idx),
    with_indices=True,
)



wildlife_test_ds = wildlife_test_ds.map(
    lambda record, idx: update_record(record, idx),
    with_indices=True,
)

repo_id = "SeaSponge/wildme_dataset"
assert num_shards == 4, f"Incorrect num_shards value, expected 4, got -> {num_shards}"

wildlife_dataset = DatasetDict({
    "train": wildlife_train_ds,
    "validation": wildlife_val_ds,
    "test": wildlife_test_ds
})


# wildlife_train_ds.to_parquet(f"wildlife_train_shard_{idx}.parquet")
# wildlife_val_ds.to_parquet(f"wildlife_val_shard_{idx}.parquet")
# wildlife_train_ds.to_parquet(f"wildlife_train_shard_{idx}.parquet")
wildlife_dataset.push_to_hub("SeaSponge/wildme_dataset",
                             max_shard_size="1GB",
                             num_shards={"train": 10, "validation": 4, "test": 2})