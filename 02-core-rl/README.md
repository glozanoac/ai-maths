# Phase 02 -- Core Reinforcement Learning Theory

Formal development of reinforcement learning from first principles: Markov decision processes, temporal-difference methods, and policy gradient algorithms. 20 lessons organized into 3 subdomains.

## Reference Textbooks

- **MDPs:** Puterman Ch.2-6, 8; Bertsekas & Tsitsiklis Ch.1-4
- **RL Algorithms:** Sutton & Barto (full); Bertsekas & Tsitsiklis Ch.2-6; Szepesvari Ch.1-4
- **Policy Gradient:** Sutton & Barto Ch.13; Sutton et al. 2000, Kakade 2002, Schulman et al. 2015

## Lessons

### 2.1 Markov Decision Processes (Lessons 39-46)

| Lesson | File | Topic | Pages |
|--------|------|-------|-------|
| 39 | `01-mdp/lesson-39-mdp-model-and-policies` | MDP components, policies, value functions, Bellman expectation equations | 10 |
| 40 | `01-mdp/lesson-40-finite-horizon-mdp` | Finite-horizon optimality equations, backward induction | 9 |
| 41 | `01-mdp/lesson-41-discounted-reward-bellman-equations` | Discounted reward criterion, Bellman optimality equation | 10 |
| 42 | `01-mdp/lesson-42-contraction-and-value-iteration` | Banach fixed-point, value iteration convergence, error bounds | 11 |
| 43 | `01-mdp/lesson-43-vi-error-bounds-and-monotonicity` | Span seminorm, monotone convergence, policy convergence | 10 |
| 44 | `01-mdp/lesson-44-average-reward-mdp` | Average reward, gain-bias equations, Blackwell optimality | 11 |
| 45 | `01-mdp/lesson-45-policy-iteration` | Policy improvement theorem, policy iteration, finite convergence | 14 |
| 46 | `01-mdp/lesson-46-lp-formulation-and-occupancy` | LP formulation, occupancy measures, constrained MDPs | 15 |

### 2.2 TD Learning (Lessons 47-53)

| Lesson | File | Topic | Pages |
|--------|------|-------|-------|
| 47 | `02-rl-algorithms/lesson-47-td0-and-nstep-td` | TD(0), TD error, convergence via SA, n-step returns | 11 |
| 48 | `02-rl-algorithms/lesson-48-td-lambda-eligibility-traces` | Lambda-return, eligibility traces, forward-backward equivalence | 11 |
| 49 | `02-rl-algorithms/lesson-49-sarsa` | SARSA, on-policy TD control, GLIE, convergence | 10 |
| 50 | `02-rl-algorithms/lesson-50-q-learning` | Q-learning, off-policy convergence, Double Q-learning, Expected SARSA | 12 |
| 51 | `02-rl-algorithms/lesson-51-function-approximation` | Linear FA, MSVE, semi-gradient TD(0), convergence under linear FA | 11 |
| 52 | `02-rl-algorithms/lesson-52-approximate-policy-iteration` | Approximate PI, error propagation, LSTD, fitted value iteration | 11 |
| 53 | `02-rl-algorithms/lesson-53-deadly-triad` | Deadly triad, Baird's counterexample, MSPBE, GTD2 | 12 |

### 2.3 Policy Gradient (Lessons 54-58)

| Lesson | File | Topic | Pages |
|--------|------|-------|-------|
| 54 | `03-policy-gradient/lesson-54-policy-gradient-theorem` | Policy gradient theorem, score function, compatible FA | 11 |
| 55 | `03-policy-gradient/lesson-55-reinforce-and-baselines` | REINFORCE, baselines, optimal baseline, variance reduction | 11 |
| 56 | `03-policy-gradient/lesson-56-natural-policy-gradient` | Natural gradient, Fisher information, covariance theorem | 11 |
| 57 | `03-policy-gradient/lesson-57-actor-critic-and-gae` | Actor-critic, advantage functions, GAE, two-timescale convergence | 11 |
| 58 | `03-policy-gradient/lesson-58-policy-gradient-synthesis` | Unified PG framework, variance taxonomy, connections to Phase 04 | 17 |

## Prerequisites

- **Phase 01** measure theory, probability, functional analysis, optimization, and game theory

## Internal Reading Order

```
MDP: 39 -> 40 -> 41 -> 42 -> 43 -> 44 -> 45 -> 46
TD:  46 -> 47 -> 48 -> 49 -> 50 -> 51 -> 52 -> 53
PG:  53 -> 54 -> 55 -> 56 -> 57 -> 58
```

Lesson 58 (synthesis) leads into Phase 04 (trust-region and proximal methods).
