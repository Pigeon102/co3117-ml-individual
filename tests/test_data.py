"""Leakage checks for the frozen protocol. Skipped if the dataset is not downloaded."""
import numpy as np
import pytest

from src import data

pytestmark = pytest.mark.skipif(not data.HAR_DIR.exists(), reason="run: python -m src.data --download")


def test_train_val_subject_disjoint():
    d = data.train_val_split()
    assert set(d["s_train"]).isdisjoint(d["s_val"])
    assert len(np.unique(d["s_val"])) == data.N_VAL_SUBJECTS


def test_train_test_subject_disjoint():
    _, _, s_train = data.load_train()
    _, _, s_test = data.load_sealed_test()
    assert set(s_train).isdisjoint(s_test)


def test_split_is_deterministic():
    a, b = data.train_val_split(), data.train_val_split()
    assert np.array_equal(a["val_idx"], b["val_idx"])


def test_shapes_and_labels():
    X, y, s = data.load_train()
    assert X.shape[1] == 561 and len(X) == len(y) == len(s)
    assert set(np.unique(y)) == set(data.LABELS)
