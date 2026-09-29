"""Frozen data protocol for UCI HAR (see data/README.md).

Test data is only reachable through `load_sealed_test()`; use it for the final comparison only.
"""
import argparse
import io
import urllib.request
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
HAR_DIR = RAW_DIR / "UCI HAR Dataset"
URL = "https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip"

SEED = 3117
N_VAL_SUBJECTS = 5

LABELS = {
    1: "WALKING",
    2: "WALKING_UPSTAIRS",
    3: "WALKING_DOWNSTAIRS",
    4: "SITTING",
    5: "STANDING",
    6: "LAYING",
}
INERTIAL_SIGNALS = [
    "body_acc_x", "body_acc_y", "body_acc_z",
    "body_gyro_x", "body_gyro_y", "body_gyro_z",
    "total_acc_x", "total_acc_y", "total_acc_z",
]


def download(force=False):
    """Download and extract UCI HAR into data/raw/ (the UCI zip contains a nested zip)."""
    if HAR_DIR.exists() and not force:
        print(f"Already present: {HAR_DIR}")
        return HAR_DIR
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {URL} ...")
    with urllib.request.urlopen(URL) as resp:
        outer = zipfile.ZipFile(io.BytesIO(resp.read()))
    inner_name = next((n for n in outer.namelist() if n.endswith(".zip")), None)
    archive = zipfile.ZipFile(io.BytesIO(outer.read(inner_name))) if inner_name else outer
    archive.extractall(RAW_DIR)
    print(f"Extracted to {HAR_DIR}")
    return HAR_DIR


def feature_names():
    names = pd.read_csv(HAR_DIR / "features.txt", sep=r"\s+", header=None)[1].tolist()
    # features.txt contains duplicate names; make them unique by suffixing the column index
    return [f"{i}_{n}" for i, n in enumerate(names)]


def _read_matrix(path):
    return pd.read_csv(path, sep=r"\s+", header=None).to_numpy(dtype=np.float64)


def _read_vector(path):
    return pd.read_csv(path, header=None)[0].to_numpy(dtype=np.int64)


def _load_partition(part):
    d = HAR_DIR / part
    X = _read_matrix(d / f"X_{part}.txt")
    y = _read_vector(d / f"y_{part}.txt")
    subjects = _read_vector(d / f"subject_{part}.txt")
    return X, y, subjects


def _load_inertial_partition(part):
    d = HAR_DIR / part / "Inertial Signals"
    channels = [_read_matrix(d / f"{s}_{part}.txt") for s in INERTIAL_SIGNALS]
    return np.stack(channels, axis=-1)  # (n_windows, 128, 9)


def load_train():
    """Static 561-feature view of the official training population: X, y, subjects."""
    if not HAR_DIR.exists():
        raise FileNotFoundError("Dataset missing. Run: python -m src.data --download")
    return _load_partition("train")


def load_train_inertial():
    """Raw inertial view of the training population: (n, 128, 9), same row order as load_train()."""
    return _load_inertial_partition("train")


def train_val_split(seed=SEED, n_val_subjects=N_VAL_SUBJECTS):
    """Subject-disjoint train/validation split inside the training population.

    Returns dict with X_train, y_train, s_train, X_val, y_val, s_val, train_idx, val_idx.
    Row order within each partition is preserved (needed for sequence views).
    """
    X, y, s = load_train()
    rng = np.random.default_rng(seed)
    val_subjects = np.sort(rng.choice(np.unique(s), size=n_val_subjects, replace=False))
    val_mask = np.isin(s, val_subjects)
    train_idx, val_idx = np.flatnonzero(~val_mask), np.flatnonzero(val_mask)
    return {
        "X_train": X[train_idx], "y_train": y[train_idx], "s_train": s[train_idx],
        "X_val": X[val_idx], "y_val": y[val_idx], "s_val": s[val_idx],
        "train_idx": train_idx, "val_idx": val_idx, "val_subjects": val_subjects,
    }


def sequences_by_subject(X, y, subjects):
    """Ordered/structured view for HMM/CRF: list of (X_seq, y_seq, subject) in original file order."""
    out = []
    for subj in pd.unique(subjects):
        m = subjects == subj
        out.append((X[m], y[m], int(subj)))
    return out


def load_sealed_test():
    """SEALED official test population (9 subjects). Final comparison only — never for tuning."""
    return _load_partition("test")


def load_sealed_test_inertial():
    return _load_inertial_partition("test")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="UCI HAR data utilities")
    ap.add_argument("--download", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    if args.download:
        download(force=args.force)
    X, y, s = load_train()
    split = train_val_split()
    print(f"train population: X={X.shape}, subjects={len(np.unique(s))}")
    print(f"train/val: {split['X_train'].shape[0]} / {split['X_val'].shape[0]} windows, "
          f"val subjects = {split['val_subjects'].tolist()}")
