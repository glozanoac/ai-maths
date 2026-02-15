# Phase 01 -- Mathematical Foundations

Rigorous treatment of the mathematical tools underpinning all subsequent phases: measure-theoretic probability, functional analysis, optimization theory, and game theory. These documents establish the formal language and proof techniques used throughout the curriculum.

## Reference Textbooks

- **Measure Theory & Probability:** Durrett Ch.1-6, Billingsley Ch.1-7
- **Functional Analysis:** Kreyszig Ch.1-5
- **Optimization:** Boyd & Vandenberghe Ch.2-11, Nesterov Ch.1-4, Borkar Ch.1-6
- **Game Theory:** Fudenberg & Tirole Ch.1-3, 6, 12-13

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| `01-measure-spaces` | `01-measure-theory/` | sigma-algebras, measures, Caratheodory extension, measurable functions, pi-lambda theorem | **exists** |
| `probability-foundations` | `01-measure-theory/` | Expectation, conditional expectation, tower property, variance, convergence modes, inequalities, Borel-Cantelli, LLN, CLT, Markov chains, martingales | **exists** |
| `01-metric-and-normed-spaces` | `02-functional-analysis/` | Metric spaces, normed spaces, Banach spaces, completeness, compactness in normed spaces | **exists** |
| `02-hilbert-spaces-and-operators` | `02-functional-analysis/` | Inner product spaces, Hilbert spaces, orthogonal projections, Riesz representation, Hahn-Banach, uniform boundedness, fixed point theorems (Banach, Brouwer, Schauder, Kakutani) | **exists** |
| `01-convex-analysis` | `03-optimization/` | Convex sets, convex functions, operations preserving convexity, conjugate functions, separation theorems | **exists** |
| `02-convex-optimization-and-duality` | `03-optimization/` | Convex optimization problems, Lagrangian duality, KKT conditions, gradient descent, accelerated methods, proximal methods, interior point methods | **exists** |
| `03-stochastic-approximation` | `03-optimization/` | Robbins-Monro, ODE method, Borkar-Meyn stability, convergence rates, Polyak-Ruppert averaging, two-timescale SA, linear SA | **exists** |
| `01-static-and-extensive-form-games` | `04-game-theory/` | Normal-form games, Nash equilibrium, minimax theorem, correlated equilibrium, extensive-form games, subgame perfection | **exists** |
| `02-repeated-games-and-incomplete-info` | `04-game-theory/` | Repeated games, folk theorems, fictitious play, no-regret learning, Bayesian games, PBE, signaling games, potential games | **exists** |

## Prerequisites

- **Phase 00** (or equivalent background in real analysis, linear algebra, probability)

## Internal Reading Order

```
01-measure-spaces -> probability-foundations
01-metric-and-normed-spaces -> 02-hilbert-spaces-and-operators
01-convex-analysis -> 02-convex-optimization-and-duality -> 03-stochastic-approximation
01-static-and-extensive-form-games -> 02-repeated-games-and-incomplete-info
```

Measure theory and probability should be read first. The remaining tracks (functional analysis, optimization, game theory) can be read in any order after measure theory, though optimization benefits from functional analysis background. Stochastic approximation requires probability foundations (martingales, convergence modes, LLN).
