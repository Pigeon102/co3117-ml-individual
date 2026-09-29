# PRE-RELEASE catch-up — W01–W04 (Foundations + Decision Tree)

- **Written on:** `YYYY-MM-DD` (actual date — no back-dating)
- **Target length:** 500–900 words · **Time cap:** ~2–3 h total
- **Before-assistance evidence:** [release-day baseline diagnostic](../../exercises/release-baseline-w01-w02.pdf) (commit `<hash>`)

## 1. Foundations (Ch.1)
- ML workflow for this use case (data → split → preprocess → model → evaluate)
- Model taxonomy (supervised/unsupervised; generative/discriminative; parametric/non-parametric)
- Metrics: why macro-F1 for 6 activity classes
- Over/underfitting and bias–variance
- Leakage checklist → see [data/README.md](../../data/README.md)
- One train/validation-curve diagnosis: `results/figures/<file>.png` (commit `<hash>`)

## 2. Decision Tree (Ch.2, Depth B)
- Own impurity/split routine: `src/from_scratch/<file>.py` (commit `<hash>`)
- Dissected tree implementation: ML-From-Scratch `<file:function>`
- Continuous attributes, missing values
- Stopping/pruning comparison (one controlled experiment): `experiments/part1_pre_midterm/<file>.py`
- Benchmark vs scikit-learn `DecisionTreeClassifier`

## 3. Written-exam capsule (4–8 sentences, no code)

## 4. Baseline diagnostic corrections
Link: `exercises/release-baseline-corrections.md`

## 5. Reflection
