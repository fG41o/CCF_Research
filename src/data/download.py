import argparse
import os
import urllib.request
from src.utils.io import ensure_dir, read_yaml

def download_file(url: str, dest: str):
    ensure_dir(os.path.dirname(dest))
    if os.path.exists(dest):
        print(f"[download] already exists: {dest}")
        return
    print(f"[download] downloading from {url}")
    urllib.request.urlretrieve(url, dest)
    size_mb = os.path.getsize(dest) / (1024 * 1024)
    print(f"[download] saved to {dest} ({size_mb:.2f} MB)")

def main(cfg_path: str):
    cfg = read_yaml(cfg_path)
    url = cfg["url"]
    raw_path = cfg["raw_path"]
    download_file(url, raw_path)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    args = p.parse_args()
    main(args.config)