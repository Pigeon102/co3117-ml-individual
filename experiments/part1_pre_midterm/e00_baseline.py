"""Protocol baselines kept all semester (Ch.1, Depth C).

Question: what macro-F1 does a trivial and a standard linear model reach on the frozen validation split?
Run: python -m experiments.part1_pre_midterm.e00_baseline
"""
import time

from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from src.data import SEED, train_val_split
from src.metrics import evaluate, log_result

MODELS = {
    "majority_class": DummyClassifier(strategy="most_frequent"),
    "sklearn_logreg": make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, random_state=SEED)),
}


def main():
    d = train_val_split()
    for name, model in MODELS.items():
        t0 = time.perf_counter()
        model.fit(d["X_train"], d["y_train"])  # scaler is fit on train only (inside the pipeline)
        t1 = time.perf_counter()
        pred = model.predict(d["X_val"])
        t2 = time.perf_counter()
        m = evaluate(d["y_val"], pred)
        print(f"{name:16s} macro-F1={m['macro_f1']:.4f} acc={m['accuracy']:.4f}")
        log_result(
            week="W05", model=name, chapter="1", depth="C", representation="static-561",
            split="val", seed=SEED, macro_f1=m["macro_f1"], accuracy=m["accuracy"],
            train_time_s=t1 - t0, infer_time_s=t2 - t1, notes="protocol baseline",
        )


if __name__ == "__main__":
    main()
