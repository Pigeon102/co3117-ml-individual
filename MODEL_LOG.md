# MODEL_LOG — per-model records (spec §9.1)

Copy the template below once per model family. Keep entries short; link to code, posts, figures, and commits instead of repeating them.

## Template

### <Model name> — Ch.<n> — Depth <A|B|C>

- **Objective / factorization / decision rule:**
- **Assumptions & inductive bias:**
- **Expected failure modes:**
- **Representation & preprocessing:** (static 561-feature / raw inertial / ordered sequence; scaler fit on train only)
- **Own pre-reference commit:** `<hash>`
- **Reference consulted (exact file/function/notebook):**
- **Code mapping (≥3 steps):**

  | Step (equation / algorithm) | Own code | Reference code |
  | --- | --- | --- |
  |  |  |  |

- **Modification made (Depth B):**
- **Hyperparameters & selection procedure:** (search space, criterion = validation macro-F1)
- **Results:** val macro-F1 / accuracy / train time / inference time / model size → row(s) in `results/metrics.csv`
- **Diagnostic plot/table + focused experiment:**
- **Error / limitation analysis (≥5 errors or one systematic confusion):**
- **Use-case fit:**
- **Exam-ready paragraph (no code):**

---

## Models

| Model | Ch. | Depth | Part | Record |
| --- | --- | --- | --- | --- |
| Majority-class baseline | 1 | C | I | _(protocol baseline, kept all semester)_ |
| Decision Tree (impurity/split routine) | 2 | B | I | TODO |
| Perceptron / Delta rule | 3 | A | I | TODO |
| MLP + backprop | 3 | A | I | TODO |
| Naive Bayes | 4 | A | I | TODO |
| Genetic Algorithm (feature selection) | 5 | B | I | TODO |
| Bayesian Network / TAN | 6 | C / theory | I | TODO |
| HMM (Forward or Viterbi core) | 6 | A (core) + B | II | TODO |
| SVM (linear, soft margin, kernel) | 7 | B + C | II | TODO |
| PCA | 8 | A | II | TODO |
| LDA | 8 | C | II | TODO |
| Bagging / AdaBoost | 9 | B + C | II | TODO |
| Logistic / softmax (MaxEnt) | 10 | A | II | TODO |
| CRF (or suitability study) | 10 | C | II | TODO |
