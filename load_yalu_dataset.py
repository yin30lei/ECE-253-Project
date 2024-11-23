from datasets import load_dataset
from pathlib import Path

# ! use streaming=True to disable downloads
wildlife_ds = load_dataset("SeaSponge/wildme_dataset", cache_dir=Path.cwd() / "yalu_dataset", streaming=True)

# * This actually works (downside, 300MB dataset shards)
print("DS from Yalu's modified dataset repo")
print(wildlife_ds)