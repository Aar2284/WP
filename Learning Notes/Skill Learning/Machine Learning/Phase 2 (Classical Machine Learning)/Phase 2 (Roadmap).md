# Classical Machine Learning

#ml/phase-2 #ml/classical

> [!abstract] Goal Master the "bread and butter" ML algorithms that still power production systems worldwide. Learn _why_ they work, not just how to call them.

**← [[Phase 1 (Roadmap)]] | → [[Phase 3 - Deep Learning Fundamentals]]**

---

## 📐 2.1 Core Concepts First

- [ ] [[The Machine Learning Workflow#^d16a07|The ML pipeline: data → features → model → evaluation → iterate]]  
- [ ] Supervised vs Unsupervised vs Reinforcement Learning
- [ ] **Bias-variance tradeoff** (one of the most important ideas in ML)
- [ ] Overfitting, underfitting, regularization (L1/L2)
- [ ] Cross-validation (k-fold)
- [ ] Train / validation / test splits
- [ ] Feature engineering & selection
- [ ] Handling missing data, outliers, imbalanced classes

---

## 📊 2.2 Supervised Learning

### Regression

- [ ] **Linear Regression** — OLS, cost function, normal equation
- [ ] **Polynomial Regression** — when linear isn't enough
- [ ] **Ridge (L2) & Lasso (L1) Regression** — regularization in practice
- [ ] **Elastic Net** — combining L1 and L2
- [ ] Evaluation metrics: MSE, RMSE, MAE, R²

### Classification

- [ ] **Logistic Regression** — sigmoid, log-loss, decision boundary
- [ ] **Support Vector Machines (SVM)** — kernel trick, margin maximization
- [ ] **K-Nearest Neighbors (KNN)** — lazy learner, curse of dimensionality
- [ ] **Naive Bayes** — probabilistic classifiers, text classification
- [ ] Evaluation metrics: accuracy, precision, recall, F1, AUC-ROC, confusion matrix

### Tree-Based Methods ⭐

- [ ] **Decision Trees** — splitting criteria (Gini, entropy), pruning
- [ ] **Random Forests** — bagging, feature importance
- [ ] **Gradient Boosting Machines (GBM)**
- [ ] **XGBoost / LightGBM / CatBoost** — the Kaggle kings, still widely used
- [ ] Understanding ensemble methods: bagging vs boosting vs stacking

---

## 🔍 2.3 Unsupervised Learning

- [ ] **K-Means Clustering** — Lloyd's algorithm, inertia, elbow method
- [ ] **Hierarchical Clustering** — dendrograms, linkage
- [ ] **DBSCAN** — density-based, handles noise
- [ ] **PCA (Principal Component Analysis)** — dimensionality reduction, explained variance
- [ ] **t-SNE & UMAP** — non-linear dimensionality reduction for visualization
- [ ] **Gaussian Mixture Models (GMM)** — soft clustering, EM algorithm
- [ ] Anomaly detection basics

---

## 🧪 2.4 Practical Tools

- [ ] **scikit-learn** — the standard library (pipelines, transformers, estimators)
- [ ] `Pipeline` and `ColumnTransformer` — production-ready preprocessing
- [ ] `GridSearchCV` / `RandomizedSearchCV` — hyperparameter tuning
- [ ] `joblib` — model serialization
- [ ] Optuna / Hyperopt — modern hyperparameter optimization

---

## 🛠️ 2.5 Projects for Phase 2

> [!example] Projects
> 
> - **Titanic survival prediction** (classification, feature engineering)
> - **House price prediction** (regression, ensemble methods)
> - **Customer segmentation** (K-means, PCA visualization)
> - Kaggle competition: any "Getting Started" competition
> - Build a complete `sklearn` Pipeline from raw CSV to predictions

---

## ✅ Phase 2 Completion Checklist

- [ ] Can explain bias-variance tradeoff to someone non-technical
- [ ] Know when to use each algorithm (and when NOT to)
- [ ] Can build a full sklearn pipeline with preprocessing + model
- [ ] Have submitted at least one Kaggle competition
- [ ] Can tune hyperparameters systematically (not just randomly)

---

_Tags: #ml/phase-2 #classical-ml #sklearn #regression #classification #clustering_ _Links: [[Phase 1 - Foundations]] | [[Phase 3 - Deep Learning Fundamentals]] | [[Projects Library]]_