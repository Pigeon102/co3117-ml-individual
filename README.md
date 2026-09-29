# CO3117 — Individual Longitudinal ML Portfolio (HK261)

**One dataset, one use case, many models.**

| Item | Value |
| --- | --- |
| Student | Đặng Võ Minh Nhựt — 2452930 |
| Course | CO3117 Machine Learning, HK261, Faculty of CSE — HCMUT, VNU-HCM |
| Use case | Predict a person's current physical activity from smartphone inertial measurements; for HMM/CRF, use temporal continuity to smooth the same activity labels. |
| Dataset | UCI Human Activity Recognition Using Smartphones (dataset id 240), https://archive.ics.uci.edu/dataset/240 |
| Target | `activity` — 6 classes: WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING |
| Primary metric | Macro-F1 (secondary: accuracy + confusion matrix) |
| Split | Subject-disjoint (see [data/README.md](data/README.md)); test set sealed until final comparison |
| Progress dashboard | [PROGRESS.md](PROGRESS.md) |

## Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python -m src.data --download        # fetches UCI HAR into data/raw/ (git-ignored)
pytest -q                            # sanity tests (split leakage, etc.)
python -m experiments.part1_pre_midterm.e00_baseline   # simple baseline -> results/metrics.csv
```

Optional wiki site: `pip install mkdocs && mkdocs serve`.

## Repository map

| Path | Purpose |
| --- | --- |
| `PROGRESS.md` | One row per Course Week: post, drill, first-attempt commit, revision commit, tag |
| `MODEL_LOG.md` | Required per-model record (spec §9.1) |
| `AI_USE.md` | Every AI-assisted episode (spec §12.5) |
| `REFERENCES.md` | Every source actually used |
| `SUBMISSION_PART1.md` / `SUBMISSION_PART2.md` | Graded-part checklists and pointers |
| `docs/` | Wiki/blog knowledge dossier (pre-release catch-up + weekly posts) |
| `exercises/` | Handwritten drill scans (first attempts) + Markdown corrections |
| `exam/` | Two-A4 living exam sheet, midterm reflection, mock final |
| `src/data.py`, `src/metrics.py` | Shared, frozen data protocol and evaluation |
| `src/from_scratch/` | Depth-A student-authored implementations |
| `src/reference_adapters/` | Depth-B/C wrappers around reference/library code (with attribution) |
| `experiments/` | One script per controlled experiment, split by Part I / Part II |
| `tests/` | Unit / sanity / numerical-gradient tests |
| `results/` | `metrics.csv` (append-only master table) + `figures/` |
| `report/` | `part1_summary.pdf`, `part2_final_report.pdf` |

## Commit & tag conventions

- Message pattern: `[Wxx][type] short description`, type ∈ `baseline | theory | drill | code | exp | review | docs`.
  e.g. `[W05][drill] first attempt perceptron drill (pre-AI)`, `[W05][review] corrected after ML-From-Scratch`.
- Each ordinary week: at least **two substantive states** — first attempt (pre-reference / pre-AI) and corrected/extended state.
- Tags: `release-baseline`, `w05`, `w06`, `w07`, `w08-midterm`, `w09` … `w15`, `part1-final`, `part2-final`.
  No `w01`–`w04` tags. Never force-push / rebase a tagged checkpoint.
