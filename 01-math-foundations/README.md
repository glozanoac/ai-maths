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
| `probability-foundations` | `01-measure-theory/` | Expectation, conditional expectation, tower property, variance, MDS, Jensen, convergence modes, inequalities, Borel-Cantelli, LLN, Markov chains, martingales | **exists** |
| -- | `02-functional-analysis/` | Normed spaces, Banach spaces, Hilbert spaces, bounded operators, spectral theory | planned |
| -- | `03-optimization/` | Convex optimization, duality, gradient methods, stochastic approximation | planned |
| -- | `04-game-theory/` | Normal-form games, Nash equilibrium, extensive-form games, repeated games | planned |

## Prerequisites

None -- this is the foundational phase.

## Internal Reading Order

```
01-measure-spaces -> probability-foundations
```

The remaining topics (functional analysis, optimization, game theory) can be read in any order after measure theory, though optimization benefits from functional analysis background.
