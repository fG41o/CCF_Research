import argparse
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils.io import ensure_dir, read_yaml

def main(cfg_path: str):
    cfg = read_yaml(cfg_path)
    raw_path = cfg["raw_path"]
    proc_dir = cfg["processed_dir"]
    target = cfg.get("target_col", "Class")
    test_size = cfg.get("test_size", 0.2)
    random_state = cfg.get("random_state", 42)

    assert os.path.exists(raw_path), f"Raw data not found: {raw_path}"
    df = pd.read_csv(raw_path)
    assert target in df.columns, f"Target column '{target}' not in data!"

    train_df, test_df = train_test_split(
        df, test_size=test_size, random_state=random_state, stratify=df[target]
    )

    ensure_dir(proc_dir)
    train_path = os.path.join(proc_dir, "train.csv")
    test_path = os.path.join(proc_dir, "test.csv")
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

    print(f"[split] train -> {train_path} ({len(train_df)})")
    print(f"[split] test  -> {test_path} ({len(test_df)})")
    print(f"[split] positive rate (train/test): "
          f"{train_df[target].mean():.4f} / {test_df[target].mean():.4f}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    args = p.parse_args()
    main(args.config)