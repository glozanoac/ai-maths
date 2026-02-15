# Rigorous Mathematics for AI/ML

A self-contained collection of mathematical documents covering the theoretical foundations of artificial intelligence and machine learning -- from measure theory through deep reinforcement learning to aerospace applications. Each document develops concepts with graduate-level rigor, provides complete proofs, and connects abstract results to learning algorithms.

## Objective

Develop a unified mathematical reference where every theorem is proved, every algorithm has a convergence analysis, and every approximation has explicit error bounds -- then implement each algorithm from scratch, grounded in this theory.

## Curriculum

The collection spans **46 documents** organized across **7 phases**. Each phase directory contains its own `README.md` with reference textbooks and reading order.

| Phase | Topic | Docs | Status |
|-------|-------|------|--------|
| **00** | Prerequisites (real analysis, linear algebra, probability) | 12 | complete |
| **01** | Mathematical Foundations (measure theory, functional analysis, optimization, game theory) | 9 | complete |
| **02** | Core RL (MDPs, TD learning, policy gradients) | 4 | 2 of 4 |
| **03** | Deep Learning (approximation theory, RNNs, LSTMs, optimization) | 4 | 2 of 4 |
| **04** | Deep RL (value-based, policy-based, model-based) | 7 | 2 of 7 |
| **05** | Multi-Agent RL (stochastic games, cooperative/competitive, mean-field) | 5 | planned |
| **06** | Aerospace Applications (control, safety, POMDPs, sim-to-real) | 5 | planned |

## Dependency Graph

```
Phase 00: Prerequisites Review
  real-analysis --> linear-algebra --> probability
        |
        v
Phase 01: Mathematical Foundations
  measure-theory --> probability-foundations
  metric-and-normed-spaces --> hilbert-spaces-and-operators
  convex-analysis --> convex-optimization --> stochastic-approximation
  static-and-extensive-form-games --> repeated-games-and-incomplete-info
        |
        v
Phase 02: Core RL                    Phase 03: Deep Learning
  MDP --> TD Learning --> PG            RNN --> LSTM
                                        approximation-theory
        |                               sgd-and-adaptive-methods
        +-------------------------------+
        |
        v
Phase 04: Deep RL              Phase 05: MARL
  value-based                    stochastic-games
  policy-based (TRPO, PPO)       cooperative / competitive
  model-based                    mean-field / communication
        |                        |
        +------------------------+
        |
        v
Phase 06: Aerospace Applications
  continuous-control, safety, POMDPs, sim-to-real, multi-vehicle
```

## Getting Started

1. **Phase 00** if your undergraduate analysis, linear algebra, or probability is rusty; otherwise skip to Phase 01.
2. **Phase 01** starting with measure theory, then follow the dependency graph.
3. Each document lists its prerequisites -- do not skip ahead, as later proofs build on earlier results.
