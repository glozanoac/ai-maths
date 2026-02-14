# Rigorous Mathematics for AI/ML

A self-contained collection of mathematical treatises covering the theoretical foundations of artificial intelligence and machine learning — from measure theory through deep reinforcement learning to aerospace applications. Every result is stated precisely and proved in full; no hand-waving, no "it can be shown that."

## Motivation

Most AI/ML resources fall into one of two categories: applied tutorials that skip the mathematics, or pure mathematics textbooks that never connect to learning algorithms. This collection bridges the gap by developing every concept with the same rigor found in a graduate mathematics course while maintaining a clear line of sight toward reinforcement learning, deep learning, and their applications.

The goal is not to replace textbooks but to distill, unify, and extend their key results into a single coherent reference — one where every theorem has a proof, every algorithm has a convergence analysis, and every approximation has explicit error bounds.

The ultimate intent is to implement every algorithm from scratch — not to call opaque library functions, but to write each update rule, each gradient computation, and each optimization loop ourselves, grounded in the theory developed here. Understanding the mathematics is what makes that possible: when you know *exactly* what an algorithm does and *why* it converges, you can build it yourself, debug it yourself, and extend it yourself, without depending on frameworks that hide the details.

## Approach

Each document follows a strict methodology:

- **Formal definitions** grounded in measure theory and functional analysis
- **Complete proofs** — no steps are omitted or left as exercises
- **Explicit assumptions** stated before every theorem, with counterexamples when assumptions are relaxed
- **Connections to practice** highlighted through dedicated remarks that link abstract results to RL algorithms, neural network training, and real-world systems

Documents are written in LaTeX and compiled to PDF. Source `.tex` files are included for recent documents.

## Intended Audience

This collection is written for readers who have:

- **Undergraduate real analysis and linear algebra** (at the level of Rudin's *Principles* and Axler's *Linear Algebra Done Right*)
- **Basic probability** (at the level of a first undergraduate course, e.g., Ross's *A First Course in Probability*)
- **Mathematical maturity** — comfort with epsilon-delta arguments, proof by induction, and abstract algebraic structures

It is aimed at:

- Graduate students in machine learning, control theory, or applied mathematics who want a unified theoretical reference
- Researchers transitioning into RL or deep learning who need to understand the proofs behind the algorithms
- Engineers and practitioners who want to go beyond the "cookbook" level and understand *why* methods work and *when* they fail

No prior knowledge of reinforcement learning, deep learning, or measure theory is assumed — Phase 01 builds these from scratch. If your undergraduate real analysis, linear algebra, or probability is rusty, Phase 00 provides a rigorous refresher to get you back up to speed before diving in.

## Curriculum Overview

The collection spans **29 documents** organized across **7 phases** (Phase 00 prerequisites + Phases 01-06 aligned with a 102-session study curriculum). Documents within each phase have explicit prerequisites and a recommended reading order.

| Phase | Topic | Documents | Status |
|-------|-------|-----------|--------|
| **00** | Prerequisites Review | Real analysis, linear algebra, probability (rigorous refresher) | planned |
| **01** | Mathematical Foundations | Measure theory, probability, functional analysis, optimization, game theory | 2 of 5 complete |
| **02** | Core Reinforcement Learning | MDPs, TD learning, policy gradients (REINFORCE, TRPO, PPO) | 4 of 5 complete |
| **03** | Deep Learning | RNNs, LSTMs, optimization for deep learning | 2 of 3 complete |
| **04** | Deep Reinforcement Learning | Value-based, policy-based, and model-based deep RL | planned |
| **05** | Multi-Agent RL | Stochastic games, cooperative/competitive MARL, mean-field games | planned |
| **06** | Aerospace Applications | Continuous control, safety, POMDPs, sim-to-real, multi-vehicle | planned |

Each phase directory contains its own `README.md` with reference textbooks, document details, and internal reading order.

## Dependency Graph

```
Phase 00: Prerequisites Review (optional)
  real-analysis --> linear-algebra --> probability
        |
        v
Phase 01: Mathematical Foundations
  measure-spaces --> probability-foundations
                 \-> functional-analysis (planned)
                 \-> optimization (planned)
                 \-> game-theory (planned)
        |
        v
Phase 02: Core RL                    Phase 03: Deep Learning
  MDP --> TD Learning --> PG            RNN --> LSTM
    --> TRPO --> PPO                    optimization-for-dl (planned)
        |                                |
        +--------------------------------+
        |
        v
Phase 04: Deep RL              Phase 05: MARL
  value-based (planned)          stochastic-games (planned)
  policy-based (planned)         cooperative (planned)
  model-based (planned)          competitive (planned)
        |                        mean-field (planned)
        +------------------------+
        |
        v
Phase 06: Aerospace Applications
  continuous-control --> safety --> partial-observability
    --> sim-to-real --> multi-vehicle
```

## Repository Structure

```
ai-maths/
  00-prerequisites/
    01-real-analysis/
    02-linear-algebra/
    03-probability/
  01-math-foundations/
    01-measure-theory/
    02-functional-analysis/
    03-optimization/
    04-game-theory/
  02-core-rl/
    01-mdp/
    02-rl-algorithms/
    03-policy-gradient/
  03-deep-learning/
    01-neural-networks/
    02-optimization-for-dl/
  04-deep-rl/
  05-marl/
  06-aerospace/
```

## Getting Started

1. **Assess your background** — if your real analysis, linear algebra, or probability feels rusty, start with Phase 00. If you can comfortably state and prove the Bolzano-Weierstrass theorem, diagonalize a symmetric matrix, and derive the variance of standard distributions, skip directly to Phase 01.
2. **Start Phase 01** — begin with `01-measure-spaces` and then `probability-foundations`. These two documents establish the mathematical language used everywhere else.
3. **Follow the dependency graph** — each document lists its prerequisites. Do not skip ahead; later proofs rely on earlier results.
4. **Read the phase READMEs** — each phase directory has a `README.md` with reference textbooks, document details, and internal reading order.
