#!/usr/bin/env python
# coding: utf-8


#!/usr/bin/env python
# coding: utf-8


import torch
import json
import ast
import torch.nn as nn
import numpy as np
from tqdm.auto import tqdm
import cv2

import matplotlib.pyplot as plt

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from transformers import ViTModel, AutoModelForObjectDetection, AutoImageProcessor, pipeline
from datasets import load_dataset
import os
import requests



# download a sample image
# ! streaming mode only gives IterableDataset (also takes some while to obtain photo)
# ! no indexing, can only iterate via for loop
wildlife_ds = load_dataset("SeaSponge/wildme_dataset", cache_dir=Path.cwd() / "yalu_dataset", streaming=True)



print(wildlife_ds["train"])
print(wildlife_ds["validation"])
print(wildlife_ds["test"])

train_ds = wildlife_ds["train"]
val_ds = wildlife_ds["validation"]
test_ds = wildlife_ds["test"]



del wildlife_ds

try:
    # object of type 'IterableDataset' has no len()
    
    # Subclasses of Dataset should implement __getitem__.
    for idx, sample in enumerate(train_ds):
        print(f"idx-> {idx} | sample -> {sample}")
        break
    
except Exception as e:
    print(f"error -> {e}")



def get_record(dataset, index):
    for i, record in enumerate(dataset):
        if i == index:
            return record
    raise IndexError("Index out of range")


# make the object detection pipeline
device = "cuda" if torch.cuda.is_available else "cpu"

hf_path = "SeaSponge/glow-model"
obj_classifier = pipeline("image-classification", model=hf_path, device=device)
# image = wildlife_ds["train"][0]["image"]

image = get_record(train_ds, 0)["image"]

# Convert to PIL and ensure it's RGB
if not isinstance(image, Image.Image):
    image = Image.fromarray(image)
image = image.convert("RGB") 

print("image")
print(image)
print(obj_classifier)



# default in dataset is <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=2400x1800 at 0x21CF8A7EB90>
results = obj_classifier(image)
# Look something like this:
# [{'label': 'leopard', 'score': 0.9535987377166748}, {'label': 'hyena', 'score': 0.0581585057079792}]
# [{'label': 'hyena', 'score': 0.8872979283332825}, {'label': 'leopard', 'score': 0.11568226665258408}]
print(f"results for first image -> {results}")



def plot_results(image, results, threshold=0.7):
    image = Image.fromarray(np.uint8(image))
    width, height = image.size
    draw = ImageDraw.Draw(image)
    best_score = 0.0
    best_res = f"[{results[0]['label']} : {round(results[0]['score'] * 100), 2}%]"
    for idx, result in enumerate(results):
        label, score = result["label"], result["score"]
        if score > best_score:
            best_score = score
            best_res = f"[{label} : {round(best_score * 100, 2)}%]"
        
    draw.text((10, 10), text=best_res,
              fill=(156, 189, 255, 255) if best_score > threshold else (181, 22, 85, 255),
              font_size=84)
    return image


def predict(image, pipeline, threshold=0.7, verbose=False):
    results = pipeline(image)
    if verbose:
        print(results)
    return plot_results(image, results, threshold)


# Let's test for another test image
iter_temp = iter(val_ds)
img = next(iter_temp)["image"]
predict(img, obj_classifier, verbose=False)        



def plot_images(dataset, indices, verbose=False):
    """
    Plot images and their annotations.
    """
    num_rows = len(indices) // 3
    num_cols = 3
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))

    for i, idx in tqdm(enumerate(indices), total=len(indices)):
        row = i // num_cols
        col = i % num_cols

        # Draw image
        image = predict(dataset[idx]["image"], obj_classifier, verbose=verbose)

        # Display image on the corresponding subplot
        axes[row, col].imshow(image)
        axes[row, col].axis("off")

    plt.tight_layout()
    plt.show()
    
def plot_images_iterable(dataset, indices, verbose=False):
    """
    Plot images and their annotations.
    """
    num_rows = len(indices) // 3
    num_cols = 3
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))
    
    ds_iter = iter(dataset)
    for i, idx in tqdm(enumerate(indices), total=len(indices)):
        row = i // num_cols
        col = i % num_cols

        # Draw image
        image = predict(next(ds_iter)["image"], obj_classifier, verbose=verbose)

        # Display image on the corresponding subplot
        axes[row, col].imshow(image)
        axes[row, col].axis("off")

    plt.tight_layout()
    plt.show()



plot_images_iterable(train_ds, range(6), verbose=False)



def load_images_from_folder(folder, batch_size, max_images=None):
    images = []
    filenames = sorted(os.listdir(folder))  # Sort to maintain order
    count = 0  # Keep track of the number of images loaded

    for filename in filenames:
        if max_images and count >= max_images:
            break

        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path)
        if img is not None:
            images.append((img, filename))
            count += 1

        if len(images) == batch_size:  # Return a batch when size is reached
            yield images
            images = []  # Reset for next batch

    if images:  # Yield remaining images if any
        yield images



def plot_process_folder(folder, batch_size=5, max_images=None, verbose=False):
    """
    Process a folder of images in batches, with an optional limit on the number of images.

    Args:
        folder (str): Path to the folder containing images.
        batch_size (int): Number of images to process in each batch.
        max_images (int, optional): Maximum number of images to load. If None, all images are loaded.
    """
    for batch in load_images_from_folder(folder, batch_size, max_images):
        original_images, filenames = zip(*batch)
        num_rows = batch_size // 3
        num_cols = 3
        fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))

        for i in tqdm(range(batch_size)):
            row = i // num_cols
            col = i % num_cols

            # Draw image

            image = original_images[i]
            if not isinstance(image, Image.Image):
                image = Image.fromarray(image)
            image = image.convert("RGB")
            
            image = predict(image, obj_classifier, verbose=verbose)

            # print(f"axes: {axes}")

            # Display image on the corresponding subplot
            axes[row, col].imshow(image)
            axes[row, col].axis("off")

        plt.tight_layout()
        plt.show()



max_images_to_process = 9
folder_path = Path.cwd().resolve().parent / "data/hyena_separated/dark"
print(folder_path)
plot_process_folder(folder_path, batch_size=9, max_images=max_images_to_process, verbose=False)  # Adjust batch size as needed

