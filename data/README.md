# Data & frozen experimental protocol

> Status: **DRAFT** — review, then mark FROZEN at R0 (before Week 6). After freezing, do not change source, target, split, metric, or seeds.

## Source
- UCI Human Activity Recognition Using Smartphones, v1.0 (UCI id 240).
  Download: `python -m src.data --download` → `data/raw/UCI HAR Dataset/` (git-ignored).
- 30 volunteers, Samsung Galaxy S II on the waist, 50 Hz accelerometer + gyroscope,
  2.56 s windows (128 samples) with 50 % overlap.

## Representations of the SAME raw data
| View | Shape | Used by |
| --- | --- | --- |
| Static engineered features | 561 features / window | Perceptron, MLP, NB, GA, SVM, PCA/LDA, ensembles, logistic |
| Raw inertial windows | 128 × 9 per window | optional (MLP on raw signals) |
| Ordered sequence | windows ordered by subject, file order (per-subject temporal order) | HMM, CRF |

## Target
`activity` ∈ {1 WALKING, 2 WALKING_UPSTAIRS, 3 WALKING_DOWNSTAIRS, 4 SITTING, 5 STANDING, 6 LAYING}.

## Split policy (subject-aware — no person appears in two partitions)
- **Test (sealed):** the official UCI test partition, 9 subjects. Loaded only through `src.data.load_sealed_test()` and only for the final comparison.
- **Train / validation:** the official 21 training subjects; `src.data.train_val_split()` holds out `N_VAL_SUBJECTS` whole subjects for validation, chosen with `SEED`.
- Cross-validation (when needed): `GroupKFold` on subject IDs inside the training population only.

## Preprocessing rule
Every scaler / encoder / PCA / LDA / feature selector is fit on training data only, then applied to validation/test.

## Metric
Primary: macro-F1. Secondary: accuracy + confusion matrix. Runtime: train and inference wall-clock (`time.perf_counter`).

## Seeds
`SEED = 3117` (in `src/data.py`) for splits and every stochastic model; repeat runs use seeds `SEED + k`.

## Baseline kept all semester
Majority-class classifier + scikit-learn logistic regression (`experiments/part1_pre_midterm/e00_baseline.py`).

## Leakage checklist
- [ ] No subject shared across train / val / test (`tests/test_data.py`)
- [ ] Preprocessing fit on train only
- [ ] No tuning on test
- [ ] Temporal views built within each partition only
