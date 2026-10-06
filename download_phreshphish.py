"""Tai dataset PhreshPhish tu HuggingFace, chi giu cot url va label, luu CSV."""
import os

try:
    from datasets import load_dataset
except ImportError:
    print("Can cai thu vien datasets: pip install datasets")
    raise SystemExit(1)

OUT_DIR = "upload"
os.makedirs(OUT_DIR, exist_ok=True)

print("Dang tai PhreshPhish (chi stream, khong tai HTML)...")
ds = load_dataset(
    "phreshphish/phreshphish",
    split="train",
    streaming=True,
)

rows = []
for i, row in enumerate(ds):
    rows.append({"url": row["url"], "label": row["label"]})
    if (i + 1) % 50000 == 0:
        print(f"  Da doc {i+1} mau...")
    if i + 1 >= 100000:
        break

import pandas as pd
df = pd.DataFrame(rows)
print(f"\nTong: {len(df)} mau")
print(df["label"].value_counts())

out = os.path.join(OUT_DIR, "phreshphish_100k.csv")
df.to_csv(out, index=False)
print(f"Da luu: {out}")
