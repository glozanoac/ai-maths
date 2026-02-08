# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a collection of rigorous mathematical treatment documents (PDFs) covering AI/ML topics. Each document provides formal proofs, complete derivations, and theoretical foundations — not implementations or code.

## Structure

- `rl/` — Reinforcement learning theory
  - Temporal-Difference Learning (TD(0), n-step TD, TD(λ), eligibility traces, SARSA, Q-learning, function approximation, deadly triad)
  - Policy Gradient Theorem (complete formal proof with log-derivative trick, Bellman equation, recursive expansion)
  - Trust Region Policy Optimization (convergence proofs, sample complexity, Fisher information, conjugate gradient)
  - Proximal Policy Optimization (clipped surrogate objective, convergence analysis, backpropagation through actor-critic)
- `supplement/` — Prerequisite mathematical foundations
  - Expectation Cheatsheet (linearity, conditional expectation, tower property, variance, MDS, Jensen's inequality)
  - Probability Foundations (σ-algebras, independence, convergence modes, inequalities, Borel-Cantelli, LLN, Markov chains, martingale convergence, Robbins-Siegmund)
- `lessons/` — Structured lessons (102 sessions, aligned with curriculum.pdf)
  - 01: Measure Spaces (σ-algebras, measures, Carathéodory extension, measurable functions, Borel σ-algebra, π-λ theorem)
- `dl/` — Deep learning architectures
  - Recurrent Neural Networks (BPTT derivation, vanishing/exploding gradient analysis, mitigation strategies)
  - LSTM Networks (gating mechanisms, cell state dynamics, BPTT through gates, variants including GRU)

## Topic Dependencies

The documents form a logical reading order:
- **RL policy gradient track:** Policy Gradient Theorem → TRPO → PPO (each builds on the previous)
- **RL value-based track:** TD-Learning (foundational; GAE section connects to PPO/TRPO)
- **DL track:** RNN → LSTM (LSTM addresses RNN's vanishing gradient problem)
- **Supplement track:** Probability Foundations → Expectation Cheatsheet → TD-Learning (and all other RL documents)

## Conventions

- Documents are LaTeX-generated PDFs; source `.tex` files may be present for newer documents
- Commit messages reference the primary topic added
- After any modification commit the changes with a meaningful commit message.
