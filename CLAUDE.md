# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a collection of rigorous mathematical treatment documents (PDFs) covering AI/ML topics. Each document provides formal proofs, complete derivations, and theoretical foundations — not implementations or code.

## Structure

- `rl/` — Reinforcement learning theory
  - Policy Gradient Theorem (complete formal proof with log-derivative trick, Bellman equation, recursive expansion)
  - Trust Region Policy Optimization (convergence proofs, sample complexity, Fisher information, conjugate gradient)
  - Proximal Policy Optimization (clipped surrogate objective, convergence analysis, backpropagation through actor-critic)
- `dl/` — Deep learning architectures
  - Recurrent Neural Networks (BPTT derivation, vanishing/exploding gradient analysis, mitigation strategies)
  - LSTM Networks (gating mechanisms, cell state dynamics, BPTT through gates, variants including GRU)

## Topic Dependencies

The documents form a logical reading order:
- **RL track:** Policy Gradient Theorem → TRPO → PPO (each builds on the previous)
- **DL track:** RNN → LSTM (LSTM addresses RNN's vanishing gradient problem)

## Conventions

- Documents are LaTeX-generated PDFs with no source `.tex` files in the repo
- Commit messages reference the primary topic added
