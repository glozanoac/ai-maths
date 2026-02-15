# Phase 00 -- Prerequisites Review

A rigorous but concise refresher of the three pillars assumed by Phase 01: real analysis, linear algebra, and probability. Each lesson follows the Gagne's Nine Events of Instruction standard with complete proofs, worked examples, RL/ML connections, and graded exercises.

**Who needs this phase?** Readers who have completed undergraduate courses in real analysis, linear algebra, and probability but have not used the material recently. If you can immediately state the Bolzano-Weierstrass theorem, diagonalize a symmetric matrix, and derive the variance of a geometric random variable, you can skip to Phase 01. Otherwise, start here.

## Reference Textbooks

- **Real Analysis:** Rudin, *Principles of Mathematical Analysis* Ch.1-9; Abbott, *Understanding Analysis* Ch.1-7
- **Linear Algebra:** Axler, *Linear Algebra Done Right* Ch.1-10; Hoffman & Kunze Ch.1-6
- **Probability:** Ross, *A First Course in Probability* Ch.1-8; Blitzstein & Hwang, *Introduction to Probability* Ch.1-10

## Lessons

### Real Analysis (Lessons 1-4)

| Lesson | File | Topic | Pages |
|--------|------|-------|-------|
| 1 | `01-real-analysis/lesson-01-real-numbers-sequences-series` | Ordered fields, sup/inf, Archimedean property, sequences, convergence, Bolzano-Weierstrass, series, convergence tests | 11 |
| 2 | `01-real-analysis/lesson-02-topology-and-continuity` | Open/closed sets, compactness, Heine-Borel, continuity, IVT, EVT, uniform continuity | 10 |
| 3 | `01-real-analysis/lesson-03-differentiation-and-integration` | Derivatives, chain rule, MVT, Taylor's theorem, Riemann integral, FTC | 11 |
| 4 | `01-real-analysis/lesson-04-function-sequences-and-metric-spaces` | Pointwise/uniform convergence, interchange theorems, metric spaces, completeness, Banach fixed-point theorem | 13 |

### Linear Algebra (Lessons 5-8)

| Lesson | File | Topic | Pages |
|--------|------|-------|-------|
| 5 | `02-linear-algebra/lesson-05-vector-spaces-and-linear-maps` | Vector spaces, subspaces, bases, dimension, linear maps, rank-nullity, matrix representation | 12 |
| 6 | `02-linear-algebra/lesson-06-determinants-and-eigenvalues` | Determinants, cofactor expansion, eigenvalues, characteristic polynomial, diagonalization, Cayley-Hamilton | 12 |
| 7 | `02-linear-algebra/lesson-07-inner-products-and-spectral-theory` | Inner products, Cauchy-Schwarz, Gram-Schmidt, orthogonal projections, spectral theorem, positive definiteness | 12 |
| 8 | `02-linear-algebra/lesson-08-svd-norms-and-matrix-calculus` | Quadratic forms, SVD, Eckart-Young, matrix norms, condition number, matrix exponential, gradient, Jacobian, Hessian | 16 |

### Probability (Lessons 9-12)

| Lesson | File | Topic | Pages |
|--------|------|-------|-------|
| 9 | `03-probability/lesson-09-probability-spaces-and-conditioning` | Probability spaces, Kolmogorov axioms, inclusion-exclusion, conditional probability, Bayes' theorem, independence | 12 |
| 10 | `03-probability/lesson-10-random-variables-and-distributions` | Discrete RVs (Bernoulli, binomial, geometric, Poisson), continuous RVs (uniform, exponential, normal), CDFs, PDFs | 13 |
| 11 | `03-probability/lesson-11-expectation-variance-joint-distributions` | Expectation, LOTUS, variance, covariance, correlation, joint distributions, conditional expectation, tower property | 12 |
| 12 | `03-probability/lesson-12-inequalities-and-limit-theorems` | MGFs, Markov/Chebyshev/Hoeffding inequalities, WLLN, SLLN, CLT, sample complexity | 16 |

## Prerequisites

None -- this is the entry point for the entire curriculum.

## Internal Reading Order

```
01-real-analysis (Lessons 1-4) --> 02-linear-algebra (Lessons 5-8) --> 03-probability (Lessons 9-12)
```

Real analysis establishes the foundations (limits, continuity, convergence) that linear algebra and probability rely on. Linear algebra introduces the finite-dimensional structures that probability uses for multivariate distributions and transformations. Probability ties both together and leads directly into Phase 01's measure-theoretic generalization.

## Legacy Documents

The original monolithic documents (`real-analysis.tex`, `linear-algebra.tex`, `probability.tex`) are retained in their respective directories for reference but have been superseded by the per-topic lessons above.
