# Mathematical & Python Foundations

#ml/phase-1 #ml/beginner

> [!abstract] Goal Build the mathematical intuition and programming fluency that _every_ ML concept rests on. Skip this and you'll memorize APIs without understanding what they do.

**← [[🤖 Machine Learning Roadmap]]** | **→ [[Phase 2 (Roadmap)]]**

---

## 🧮 1.1 Mathematics

### Linear Algebra

- [x] Vectors, matrices, tensors — what they represent geometrically
- [x] Matrix multiplication (the _core_ operation of all neural nets)
- [x] Dot products, norms, distance metrics
- [x] Eigenvalues & eigenvectors (used in PCA, SVD)
- [ ] Singular Value Decomposition (SVD)
- [ ] Change of basis

**Resources:**

- 📺 3Blue1Brown — [_Essence of Linear Algebra_](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) (YouTube, free)
- 📖 Gilbert Strang — _Introduction to Linear Algebra_ (MIT OpenCourseWare)
- 🧑‍💻 Practice: `numpy` matrix ops in a notebook

### Calculus & Optimization

- [ ] Derivatives and the chain rule (the backbone of backprop)
- [ ] Partial derivatives & gradients
- [ ] Gradient descent intuition — what does "descending a loss surface" mean?
- [ ] Multivariable calculus basics
- [ ] Taylor series (useful for understanding optimizers)

**Resources:**

- 📺 3Blue1Brown — _Essence of Calculus_ (YouTube, free)
- 📖 Khan Academy Calculus (free)

### Probability & Statistics

- [ ] Random variables, probability distributions
- [ ] Bayes' theorem — foundational to probabilistic ML
- [ ] Expectation, variance, covariance
- [ ] Common distributions: Gaussian, Bernoulli, Multinomial, Poisson
- [ ] Maximum Likelihood Estimation (MLE)
- [ ] Hypothesis testing, p-values, confidence intervals
- [ ] Central Limit Theorem

**Resources:**

- 📖 _Probability and Statistics for ML_ — Deep Learning book Ch. 3 (Goodfellow, free PDF)
- 🎓 StatQuest with Josh Starmer (YouTube)

---

## 🐍 1.2 Python for ML

### Core Python

- [ ] Data types, control flow, comprehensions
- [ ] Functions, `*args`, `**kwargs`, decorators
- [ ] Object-oriented programming — classes, inheritance
- [ ] File I/O, context managers
- [ ] Error handling

### Scientific Python Stack

- [ ] **NumPy** — array ops, broadcasting, vectorization
- [ ] **Pandas** — DataFrames, indexing, groupby, merge
- [ ] **Matplotlib / Seaborn** — visualization fundamentals
- [ ] **SciPy** — statistical functions, optimization utils
- [ ] Jupyter notebooks / VS Code with notebooks

**Resources:**

- 📖 _Python for Data Analysis_ — Wes McKinney
- 🧑‍💻 Kaggle Learn: Python + Pandas (free, interactive)

---

## 🛠️ 1.3 Projects for Phase 1

> [!example] Mini Projects
> 
> - Implement gradient descent **from scratch** in NumPy (no sklearn)
> - EDA (exploratory data analysis) on a Kaggle dataset using Pandas + Seaborn
> - Build a matrix class in pure Python

---

## ✅ Phase 1 Completion Checklist

- [ ] Can multiply matrices by hand and explain what the result means
- [ ] Can explain what a gradient is geometrically
- [ ] Can implement simple gradient descent from scratch
- [ ] Can load, clean, and visualize a real dataset
- [ ] Comfortable with NumPy broadcasting

---

_Tags: #ml/phase-1 #math #python #foundations_ _Links: [[Phase 2 - Classical ML]] | [[Concept Glossary]] | [[Resources & Books]]_