"""Common evaluation + append-only master results table (results/metrics.csv)."""
import csv
import datetime as dt
import subprocess
from pathlib import Path

import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

ROOT = Path(__file__).resolve().parents[1]
METRICS_CSV = ROOT / "results" / "metrics.csv"
FIELDS = [
    "date", "commit", "week", "model", "chapter", "depth", "representation",
    "split", "seed", "macro_f1", "accuracy", "train_time_s", "infer_time_s", "notes",
]
CLASS_ORDER = [1, 2, 3, 4, 5, 6]


def evaluate(y_true, y_pred):
    return {
        "macro_f1": f1_score(y_true, y_pred, average="macro", labels=CLASS_ORDER, zero_division=0),
        "accuracy": accuracy_score(y_true, y_pred),
        "confusion": confusion_matrix(y_true, y_pred, labels=CLASS_ORDER),
    }


def git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, stderr=subprocess.DEVNULL
        ).decode().strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "uncommitted"


def log_result(**row):
    """Append one row to results/metrics.csv. Never edit old rows; add new ones."""
    row.setdefault("date", dt.date.today().isoformat())
    row.setdefault("commit", git_commit())
    for k in ("macro_f1", "accuracy", "train_time_s", "infer_time_s"):
        if isinstance(row.get(k), (float, np.floating)):
            row[k] = f"{row[k]:.4f}"
    METRICS_CSV.parent.mkdir(parents=True, exist_ok=True)
    new_file = not METRICS_CSV.exists() or METRICS_CSV.stat().st_size == 0
    with open(METRICS_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="raise")
        if new_file:
            w.writeheader()
        w.writerow({k: row.get(k, "") for k in FIELDS})
