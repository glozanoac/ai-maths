# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a collection of rigorous mathematical treatment documents (PDFs) covering AI/ML topics. Each document provides formal proofs, complete derivations, and theoretical foundations — not implementations or code.

## Structure (aligned with curriculum.pdf — 6 phases, 102 sessions)

- `01-math-foundations/` — Mathematical Foundations
  - `01-measure-theory/` — Durrett Ch.1-6, Billingsley Ch.1-7
    - 01-measure-spaces (σ-algebras, measures, Carathéodory extension, measurable functions, π-λ theorem)
    - probability-foundations (convergence modes, inequalities, Borel-Cantelli, LLN, Markov chains, martingales)
    - expectation-cheatsheet (linearity, conditional expectation, tower property, variance, MDS, Jensen)
  - `02-functional-analysis/` — Kreyszig Ch.1-5
  - `03-optimization/` — Boyd Ch.2-11, Nesterov Ch.1-4, Borkar Ch.1-6
  - `04-game-theory/` — Fudenberg & Tirole Ch.1-3,6,12-13
- `02-core-rl/` — Core Reinforcement Learning Theory
  - `01-mdp/` — Puterman Ch.2-6,8, Bertsekas & Tsitsiklis Ch.1-4
  - `02-rl-algorithms/` — Sutton & Barto full, Szepesvári Ch.1-4
    - Temporal-Difference-Learning (TD(0), n-step, TD(λ), SARSA, Q-learning, function approximation, deadly triad)
  - `03-policy-gradient/` — Sutton & Barto Ch.13, Schulman et al.
    - Policy-Gradient-Theorem, Trust-Region-Policy-Optimization, Proximal-Policy-Optimization
- `03-deep-learning/` — Deep Learning Foundations
  - `01-neural-networks/` — Bach Ch.1-14, Goodfellow et al.
    - RNN (BPTT, vanishing/exploding gradients), LSTM (gating, cell state dynamics, GRU)
  - `02-optimization-for-dl/` — Bach Ch.9-14
- `04-deep-rl/` — Deep Reinforcement Learning
  - `01-value-based/` — DQN, Rainbow, distributional RL
  - `02-policy-based/` — A3C, PPO+FA, SAC
  - `03-model-based/` — Dyna, MuZero, world models
- `05-marl/` — Multi-Agent Reinforcement Learning
  - `01-stochastic-games/` — Shoham & Leyton-Brown, Filar & Vrieze
  - `02-cooperative/` — CTDE, QMIX, MAPPO
  - `03-competitive/` — minimax MARL, policy-space response oracles
  - `04-mean-field/` — Carmona & Delarue, mean-field games
  - `05-communication/` — CommNet, TarMAC, emergent communication
- `06-aerospace/` — Aerospace Applications
  - `01-continuous-control/` — continuous action spaces, Lie group methods
  - `02-safety/` — constrained MDPs, Lyapunov-based methods
  - `03-partial-observability/` — POMDPs, belief-space planning
  - `04-sim-to-real/` — domain randomization, system identification
  - `05-multi-vehicle/` — formation control, task allocation

## Reading Order

Within each phase, documents build on each other:
- **01 → 02 → 03 → 04** (sequential prerequisite chain)
- **02 + 01/04-game-theory → 05** (MARL requires both RL and game theory)
- **04 + 05 → 06** (applications integrate deep RL and multi-agent)

## Conventions

- Documents are LaTeX-generated PDFs; source `.tex` files may be present for newer documents
- Commit messages reference the primary topic added
- After any modification commit the changes with a meaningful commit message.
