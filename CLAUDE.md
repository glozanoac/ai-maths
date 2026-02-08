# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a collection of rigorous mathematical treatment documents (PDFs) covering AI/ML topics. Each document provides formal proofs, complete derivations, and theoretical foundations — not implementations or code.

## Structure (aligned with curriculum.pdf — 6 phases, 102 sessions)

- `I-math-foundations/` — Phase I: Mathematical Foundations
  - `measure-theory/` — Durrett Ch.1-6, Billingsley Ch.1-7
    - 01-measure-spaces (σ-algebras, measures, Carathéodory extension, measurable functions, π-λ theorem)
    - probability-foundations (convergence modes, inequalities, Borel-Cantelli, LLN, Markov chains, martingales)
    - expectation-cheatsheet (linearity, conditional expectation, tower property, variance, MDS, Jensen)
  - `functional-analysis/` — Kreyszig Ch.1-5
  - `optimization/` — Boyd Ch.2-11, Nesterov Ch.1-4, Borkar Ch.1-6
  - `game-theory/` — Fudenberg & Tirole Ch.1-3,6,12-13
- `II-core-rl/` — Phase II: Core Reinforcement Learning Theory
  - `mdp/` — Puterman Ch.2-6,8, Bertsekas & Tsitsiklis Ch.1-4
  - `rl-algorithms/` — Sutton & Barto full, Szepesvári Ch.1-4
    - Temporal-Difference-Learning (TD(0), n-step, TD(λ), SARSA, Q-learning, function approximation, deadly triad)
  - `policy-gradient/` — Sutton & Barto Ch.13, Schulman et al.
    - Policy-Gradient-Theorem, Trust-Region-Policy-Optimization, Proximal-Policy-Optimization
- `III-deep-learning/` — Phase III: Deep Learning Foundations
  - `neural-networks/` — Bach Ch.1-14, Goodfellow et al.
    - RNN (BPTT, vanishing/exploding gradients), LSTM (gating, cell state dynamics, GRU)
  - `optimization-for-dl/` — Bach Ch.9-14
- `IV-deep-rl/` — Phase IV: Deep Reinforcement Learning
  - `value-based/` — DQN, Rainbow, distributional RL
  - `policy-based/` — A3C, PPO+FA, SAC
  - `model-based/` — Dyna, MuZero, world models
- `V-marl/` — Phase V: Multi-Agent Reinforcement Learning
  - `stochastic-games/` — Shoham & Leyton-Brown, Filar & Vrieze
  - `cooperative/` — CTDE, QMIX, MAPPO
  - `competitive/` — minimax MARL, policy-space response oracles
  - `mean-field/` — Carmona & Delarue, mean-field games
  - `communication/` — CommNet, TarMAC, emergent communication
- `VI-aerospace/` — Phase VI: Aerospace Applications
  - `continuous-control/` — continuous action spaces, Lie group methods
  - `safety/` — constrained MDPs, Lyapunov-based methods
  - `partial-observability/` — POMDPs, belief-space planning
  - `sim-to-real/` — domain randomization, system identification
  - `multi-vehicle/` — formation control, task allocation

## Reading Order

Within each phase, documents build on each other:
- **Phase I → II → III → IV** (sequential prerequisite chain)
- **Phase II + I.game-theory → V** (MARL requires both RL and game theory)
- **Phase IV + V → VI** (applications integrate deep RL and multi-agent)

## Conventions

- Documents are LaTeX-generated PDFs; source `.tex` files may be present for newer documents
- Commit messages reference the primary topic added
- After any modification commit the changes with a meaningful commit message.
