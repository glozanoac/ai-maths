# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a collection of rigorous mathematical treatment documents (PDFs) covering AI/ML topics. Each document provides formal proofs, complete derivations, and theoretical foundations — not implementations or code.

## Document Catalog

Documents are organized across 6 phases (aligned with curriculum.pdf — 102 sessions). Each phase directory has its own `README.md` with full details.

| # | Path | Topic | Status |
|---|------|-------|--------|
| 1 | `01-math-foundations/01-measure-theory/01-measure-spaces` | σ-algebras, measures, Carathéodory extension, measurable functions, π-λ theorem | **exists** |
| 2 | `01-math-foundations/01-measure-theory/probability-foundations` | Expectation, conditional expectation, tower property, variance, MDS, Jensen, convergence modes, inequalities, Borel-Cantelli, LLN, Markov chains, martingales | **exists** |
| 3 | `01-math-foundations/02-functional-analysis/` | Normed spaces, Banach spaces, Hilbert spaces, bounded operators, spectral theory | planned |
| 4 | `01-math-foundations/03-optimization/` | Convex optimization, duality, gradient methods, stochastic approximation | planned |
| 5 | `01-math-foundations/04-game-theory/` | Normal-form games, Nash equilibrium, extensive-form games, repeated games | planned |
| 6 | `02-core-rl/01-mdp/` | MDPs, Bellman equations, value/policy iteration, contraction mappings | planned |
| 7 | `02-core-rl/02-rl-algorithms/Temporal-Difference-Learning` | TD(0), n-step TD, TD(λ), SARSA, Q-learning, function approximation, deadly triad | **exists** |
| 8 | `02-core-rl/03-policy-gradient/Policy-Gradient-Theorem` | Policy gradient theorem, REINFORCE, baseline methods | **exists** |
| 9 | `02-core-rl/03-policy-gradient/Trust-Region-Policy-Optimization` | TRPO, natural policy gradient, KL-constrained optimization | **exists** |
| 10 | `02-core-rl/03-policy-gradient/Proximal-Policy-Optimization` | PPO, clipped surrogate objective, advantage estimation | **exists** |
| 11 | `03-deep-learning/01-neural-networks/rnn` | BPTT, vanishing/exploding gradients, sequence modeling | **exists** |
| 12 | `03-deep-learning/01-neural-networks/lstm` | Gating mechanisms, cell state dynamics, GRU | **exists** |
| 13 | `03-deep-learning/02-optimization-for-dl/` | SGD analysis, Adam, learning rate schedules, batch normalization | planned |
| 14 | `04-deep-rl/01-value-based/` | DQN, Rainbow, distributional RL | planned |
| 15 | `04-deep-rl/02-policy-based/` | A3C, PPO+function approximation, SAC | planned |
| 16 | `04-deep-rl/03-model-based/` | Dyna, MuZero, world models | planned |
| 17 | `05-marl/01-stochastic-games/` | Stochastic games, Shapley value, Nash-Q | planned |
| 18 | `05-marl/02-cooperative/` | CTDE, QMIX, MAPPO | planned |
| 19 | `05-marl/03-competitive/` | Minimax MARL, policy-space response oracles | planned |
| 20 | `05-marl/04-mean-field/` | Mean-field games, McKean-Vlasov dynamics | planned |
| 21 | `05-marl/05-communication/` | CommNet, TarMAC, emergent communication | planned |
| 22 | `06-aerospace/01-continuous-control/` | Continuous action spaces, Lie group methods | planned |
| 23 | `06-aerospace/02-safety/` | Constrained MDPs, Lyapunov-based methods | planned |
| 24 | `06-aerospace/03-partial-observability/` | POMDPs, belief-space planning | planned |
| 25 | `06-aerospace/04-sim-to-real/` | Domain randomization, system identification | planned |
| 26 | `06-aerospace/05-multi-vehicle/` | Formation control, task allocation | planned |

## Dependency Tree / Reading Order

The dependency tree shows prerequisites for each document. Arrows (→) indicate "is required by".

```
Phase 01 — Mathematical Foundations
  01-measure-spaces
    → probability-foundations
    → [all Phase 02, 03 documents]
  probability-foundations
    → [all Phase 02, 03 documents]
  functional-analysis (planned)
  optimization (planned)
  game-theory (planned)
    → [Phase 05: MARL]

Phase 02 — Core Reinforcement Learning  (requires: Phase 01)
  MDP (planned)
    → Temporal-Difference-Learning
  Temporal-Difference-Learning
    → Policy-Gradient-Theorem
  Policy-Gradient-Theorem
    → Trust-Region-Policy-Optimization
  Trust-Region-Policy-Optimization
    → Proximal-Policy-Optimization

Phase 03 — Deep Learning  (requires: Phase 01; independent of Phase 02)
  rnn
    → lstm
  optimization-for-dl (planned)

Phase 04 — Deep Reinforcement Learning  (requires: Phase 02 + Phase 03)
  value-based (planned)
  policy-based (planned)
  model-based (planned)

Phase 05 — Multi-Agent RL  (requires: Phase 02 + Phase 01/04-game-theory)
  stochastic-games (planned)
  cooperative (planned)
  competitive (planned)
  mean-field (planned)
  communication (planned)

Phase 06 — Aerospace Applications  (requires: Phase 04 + Phase 05)
  continuous-control (planned)
  safety (planned)
  partial-observability (planned)
  sim-to-real (planned)
  multi-vehicle (planned)
```

**Inter-phase dependencies summary:**
- **01 → 02** : Measure theory and probability needed for RL foundations
- **01 → 03** : Measure theory and probability needed for deep learning theory
- **02 + 03 → 04** : Core RL + deep learning combine into deep RL
- **02 + 01/game-theory → 05** : MARL requires RL theory and game theory
- **04 + 05 → 06** : Aerospace applications integrate deep RL and multi-agent methods

## Conventions

- Documents are LaTeX-generated PDFs; source `.tex` files may be present for newer documents
- Commit messages reference the primary topic added
- After any modification compile and commit the changes with a meaningful commit message.
- When creating a new document, add it to the Document Catalog in this file and update the corresponding phase `README.md`.
