# Phase 00 — Prerequisites Review

A rigorous but concise refresher of the three pillars assumed by Phase 01: real analysis, linear algebra, and probability. These documents are not watered-down summaries — every theorem is stated formally and proved — but they are selective: only the results that Phase 01 and beyond actually depend on are included.

**Who needs this phase?** Readers who have completed undergraduate courses in real analysis, linear algebra, and probability but have not used the material recently. If you can immediately state the Bolzano-Weierstrass theorem, diagonalize a symmetric matrix, and derive the variance of a geometric random variable, you can skip to Phase 01. Otherwise, start here.

## Reference Textbooks

- **Real Analysis:** Rudin, *Principles of Mathematical Analysis* Ch.1-9; Abbott, *Understanding Analysis* Ch.1-7
- **Linear Algebra:** Axler, *Linear Algebra Done Right* Ch.1-10; Hoffman & Kunze Ch.1-6
- **Probability:** Ross, *A First Course in Probability* Ch.1-8; Blitzstein & Hwang, *Introduction to Probability* Ch.1-10

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| — | `01-real-analysis/` | Ordered fields, supremum/infimum, sequences and series, limits, continuity, differentiation, Riemann integration, metric spaces, compactness, uniform convergence, interchange of limits | planned |
| — | `02-linear-algebra/` | Vector spaces, linear maps, matrices, determinants, eigenvalues, diagonalization, inner product spaces, orthogonality, spectral theorem, SVD | planned |
| — | `03-probability/` | Sample spaces, axioms, conditional probability, independence, random variables, common distributions, expectation, variance, joint distributions, moment-generating functions, law of large numbers, central limit theorem | planned |

## Prerequisites

None — this is the entry point for the entire curriculum.

## Internal Reading Order

```
01-real-analysis --> 02-linear-algebra --> 03-probability
```

Real analysis establishes the foundations (limits, continuity, convergence) that linear algebra and probability rely on. Linear algebra introduces the finite-dimensional structures that probability uses for multivariate distributions and transformations. Probability ties both together and leads directly into Phase 01's measure-theoretic generalization.
