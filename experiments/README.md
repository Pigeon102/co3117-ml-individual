# Experiments

One script = one focused question. Name: `eNN_<model>_<question>.py`. Each script:
1. States the question and my prediction in its docstring (written before running).
2. Uses `src.data.train_val_split()` (never the sealed test, except the final comparison).
3. Logs results via `src.metrics.log_result(...)` and saves figures to `results/figures/`.

- `part1_pre_midterm/` — W01–W07 (Part I)
- `part2_post_midterm/` — W09–W15 (Part II); final sealed-test comparison lives here.

Run from the repo root: `python -m experiments.part1_pre_midterm.e00_baseline`
