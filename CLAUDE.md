# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a collection of rigorous mathematical treatment documents (PDFs) covering AI/ML topics. Each document provides formal proofs, complete derivations, and theoretical foundations -- not implementations or code.

## Document Catalog

Documents are organized across 7 phases (Phase 00 prerequisites + Phases 01-06 aligned with curriculum.pdf -- 102 sessions). Each phase directory has its own `README.md` with full details.

**Total: 37 documents** (13 exist, 24 planned)

### Phase 00 -- Prerequisites (3 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 1 | `00-prerequisites/01-real-analysis/real-analysis` | Ordered fields, supremum/infimum, sequences, limits, continuity, differentiation, Riemann integration, metric spaces, compactness, uniform convergence | **exists** |
| 2 | `00-prerequisites/02-linear-algebra/linear-algebra` | Vector spaces, linear maps, eigenvalues, diagonalization, inner product spaces, spectral theorem, SVD | **exists** |
| 3 | `00-prerequisites/03-probability/probability` | Axioms, conditional probability, independence, random variables, distributions, expectation, variance, LLN, CLT | **exists** |

### Phase 01 -- Mathematical Foundations (9 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 4 | `01-math-foundations/01-measure-theory/01-measure-spaces` | sigma-algebras, measures, Caratheodory extension, measurable functions, pi-lambda theorem | **exists** |
| 5 | `01-math-foundations/01-measure-theory/probability-foundations` | Expectation, conditional expectation, tower property, variance, convergence modes, inequalities, Borel-Cantelli, LLN, CLT, Markov chains, martingales | **exists** |
| 6 | `01-math-foundations/02-functional-analysis/01-metric-and-normed-spaces` | Metric spaces, normed spaces, Banach spaces, completeness, compactness in normed spaces | **exists** |
| 7 | `01-math-foundations/02-functional-analysis/02-hilbert-spaces-and-operators` | Inner product spaces, Hilbert spaces, orthogonal projections, Riesz representation, Hahn-Banach, uniform boundedness, fixed point theorems (Banach, Brouwer, Schauder, Kakutani) | **exists** |
| 8 | `01-math-foundations/03-optimization/01-convex-analysis` | Convex sets, convex functions, operations preserving convexity, conjugate functions, separation theorems | **exists** |
| 9 | `01-math-foundations/03-optimization/02-convex-optimization-and-duality` | Convex optimization problems, Lagrangian duality, KKT conditions, gradient descent, accelerated methods, proximal methods, interior point methods | **exists** |
| 10 | `01-math-foundations/03-optimization/03-stochastic-approximation` | Robbins-Monro, ODE method, convergence analysis, two-timescale SA | **exists** |
| 11 | `01-math-foundations/04-game-theory/01-static-and-extensive-form-games` | Normal-form games, Nash equilibrium, minimax theorem, correlated equilibrium, extensive-form games, subgame perfection | **exists** |
| 12 | `01-math-foundations/04-game-theory/02-repeated-games-and-incomplete-info` | Repeated games, folk theorems, fictitious play, no-regret learning, Bayesian games, PBE, signaling games, potential games | **exists** |

### Phase 02 -- Core Reinforcement Learning (4 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 13 | `02-core-rl/01-mdp/01-mdp-formulation-and-finite-horizon` | MDP model, policies, finite-horizon MDPs, backward induction | planned |
| 14 | `02-core-rl/01-mdp/02-infinite-horizon-and-dynamic-programming` | Discounted/average reward, Bellman equations, contraction, value/policy iteration, LP formulation | planned |
| 15 | `02-core-rl/02-rl-algorithms/temporal-difference-learning` | TD(0), n-step TD, TD(lambda), SARSA, Q-learning, function approximation, deadly triad | **exists** |
| 16 | `02-core-rl/03-policy-gradient/policy-gradient-theorem` | Policy gradient theorem, REINFORCE, baseline variance reduction, natural gradient, Fisher information | **exists** |

### Phase 03 -- Deep Learning (4 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 17 | `03-deep-learning/01-neural-networks/01-approximation-theory` | Universal approximation (Cybenko, Hornik), Barron's theorem, approximation rates, Rademacher complexity, NTK perspective | planned |
| 18 | `03-deep-learning/01-neural-networks/rnn` | BPTT, vanishing/exploding gradients, sequence modeling | **exists** |
| 19 | `03-deep-learning/01-neural-networks/lstm` | Gating mechanisms, cell state dynamics, GRU | **exists** |
| 20 | `03-deep-learning/02-optimization-for-dl/01-sgd-and-adaptive-methods` | SGD convergence (convex/non-convex), variance reduction, AdaGrad, RMSprop, Adam, loss landscape geometry, batch normalization | planned |

### Phase 04 -- Deep Reinforcement Learning (7 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 21 | `04-deep-rl/01-value-based/01-dqn-and-extensions` | DQN, experience replay, target networks, Double DQN, Dueling, overestimation bias | planned |
| 22 | `04-deep-rl/01-value-based/02-distributional-rl` | C51, quantile regression DQN, IQN, distributional Bellman equation | planned |
| 23 | `04-deep-rl/02-policy-based/01-trust-region-methods` | TRPO, natural policy gradient, KL-constrained optimization | **exists** |
| 24 | `04-deep-rl/02-policy-based/02-proximal-policy-optimization` | PPO, clipped surrogate objective, advantage estimation | **exists** |
| 25 | `04-deep-rl/02-policy-based/03-deterministic-policy-gradient` | Deterministic PG theorem, DDPG, TD3 | planned |
| 26 | `04-deep-rl/02-policy-based/04-maximum-entropy-rl` | Maximum entropy framework, SAC, two-timescale actor-critic analysis | planned |
| 27 | `04-deep-rl/03-model-based/01-model-based-rl` | Dyna, MuZero, Dreamer, world models, planning with learned models | planned |

### Phase 05 -- Multi-Agent RL (5 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 28 | `05-marl/01-stochastic-games/01-stochastic-game-theory` | Stochastic game formalism, Markov perfect equilibrium, Shapley's theorem, existence via fixed points | planned |
| 29 | `05-marl/02-cooperative/01-cooperative-marl` | Dec-POMDP, CTDE, VDN, QMIX, QTRAN, MAPPO, IGM condition, credit assignment | planned |
| 30 | `05-marl/03-competitive/01-competitive-and-mixed-marl` | Minimax-Q, Nash-Q, MADDPG, LOLA, self-play, PSRO | planned |
| 31 | `05-marl/04-mean-field/01-mean-field-games` | Mean field game theory, McKean-Vlasov dynamics, forward-backward SDEs, mean field equilibria | planned |
| 32 | `05-marl/05-communication/01-communication-in-marl` | CommNet, DIAL, RIAL, TarMAC, emergent communication | planned |

### Phase 06 -- Aerospace Applications (5 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 33 | `06-aerospace/01-continuous-control/01-continuous-control` | High-dimensional action spaces, hierarchical RL, MPC+RL hybrids | planned |
| 34 | `06-aerospace/02-safety/01-safety-and-constraints` | Constrained MDPs, Lagrangian relaxation, CPO, Lyapunov stability, reachability | planned |
| 35 | `06-aerospace/03-partial-observability/01-pomdps` | POMDP formulation, belief states, structural results, approximate methods | planned |
| 36 | `06-aerospace/04-sim-to-real/01-sim-to-real-transfer` | Domain randomization, system identification, progressive nets | planned |
| 37 | `06-aerospace/05-multi-vehicle/01-multi-vehicle-coordination` | Formation control (graph Laplacian), collision avoidance, communication-aware coordination | planned |

## Dependency Tree / Reading Order

The dependency tree shows prerequisites for each document. Arrows (->) indicate "is required by".

```
Phase 00 -- Prerequisites (optional refresher)
  real-analysis -> linear-algebra -> probability -> [Phase 01]

Phase 01 -- Mathematical Foundations (requires: Phase 00 or equivalent background)
  01-measure-spaces -> probability-foundations -> [Phase 02, 03]
  01-metric-and-normed-spaces -> 02-hilbert-spaces-and-operators -> [Phase 02, 04]
  01-convex-analysis -> 02-convex-optimization-and-duality -> 03-stochastic-approximation -> [Phase 02]
  01-static-and-extensive-form-games -> 02-repeated-games-and-incomplete-info -> [Phase 05]

Phase 02 -- Core RL (requires: Phase 01 measure theory + optimization)
  01-mdp-formulation -> 02-infinite-horizon-and-dp
  02-infinite-horizon-and-dp -> temporal-difference-learning
  temporal-difference-learning -> policy-gradient-theorem
  policy-gradient-theorem -> [Phase 04 policy-based]

Phase 03 -- Deep Learning (requires: Phase 01 measure theory; independent of Phase 02)
  01-approximation-theory
  rnn -> lstm
  01-sgd-and-adaptive-methods

Phase 04 -- Deep RL (requires: Phase 02 + Phase 03)
  01-dqn-and-extensions -> 02-distributional-rl
  01-trust-region-methods -> 02-proximal-policy-optimization
  03-deterministic-policy-gradient
  04-maximum-entropy-rl

Phase 05 -- MARL (requires: Phase 02 + Phase 01 game theory)
  01-stochastic-game-theory -> {cooperative, competitive, mean-field, communication}

Phase 06 -- Aerospace (requires: Phase 04 + Phase 05)
  {continuous-control, safety, partial-observability, sim-to-real, multi-vehicle}
```

**Inter-phase dependencies summary:**
- **00 -> 01** : Prerequisites review refreshes the background needed for measure theory
- **01 -> 02** : Measure theory and probability needed for RL foundations
- **01 -> 03** : Measure theory and probability needed for deep learning theory
- **02 + 03 -> 04** : Core RL + deep learning combine into deep RL
- **02 + 01/game-theory -> 05** : MARL requires RL theory and game theory
- **04 + 05 -> 06** : Aerospace applications integrate deep RL and multi-agent methods

## Conventions

- Documents are LaTeX-generated PDFs; source `.tex` files may be present for newer documents
- Commit messages reference the primary topic added
- After any modification compile and commit the changes with a meaningful commit message.
- When creating a new document, add it to the Document Catalog in this file and update the corresponding phase `README.md`.
- Only use ASCII characters to write documents.
- After creating the PDF document from tex file, clean the temporal files that were generated.

## Lesson structure
Each lesson must have the following sections:
1. Motivation and Overview: Show connections with the final objective (reinforcement learning)
2. References: References to specific chapters of books or articles to complement the lecture.
3. Sections related to the topic: Depends of the topics that is being developing
4. Exercises: Enhance and challenge the builded knowledgment (score with * the dificulty of the problem)
5. Summary: Summary of important points of the lesson
6. Furter Readings: References to furter reading (another lecture or a reference books or article)
