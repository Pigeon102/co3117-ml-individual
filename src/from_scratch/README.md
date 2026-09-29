# Depth-A implementations (student-authored)

Written by me, NumPy/Python only — no library estimator for the required mechanism.
First attempt is committed **before** opening ML-From-Scratch / numpy-ml / pyprobml or using AI.

Suggested interface (to plug into the common protocol): `fit(X, y) -> self`, `predict(X) -> np.ndarray`, optional `predict_proba(X)`.

| Module (planned) | Chapter | Required mechanism | Tests |
| --- | --- | --- | --- |
| `impurity.py` | 2 | Gini/entropy + best split on a continuous feature | known small example |
| `perceptron.py` | 3 | Perceptron + delta (LMS) rule, one-vs-rest | linearly separable toy data converges |
| `mlp.py` | 3 | Forward/backward pass, softmax cross-entropy | numerical gradient check |
| `naive_bayes.py` | 4 | Gaussian NB with variance smoothing | compare to sklearn `GaussianNB` |
| `hmm.py` | 6 | Forward and/or Viterbi (log-space) | synthetic HMM with known answer |
| `pca.py` | 8 | Covariance eigendecomposition / SVD | explained variance vs sklearn |
| `logistic.py` | 10 | Softmax regression, gradient descent | gradient check, sklearn benchmark |
