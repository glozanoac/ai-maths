# Phase 02 — Core Reinforcement Learning Theory

Formal development of reinforcement learning from first principles: Markov decision processes, temporal-difference methods, and policy gradient algorithms. Each document builds directly on its predecessor, forming a strict linear chain.

## Reference Textbooks

- **MDPs:** Puterman Ch.2-6, 8; Bertsekas & Tsitsiklis Ch.1-4
- **RL Algorithms:** Sutton & Barto (full); Szepesvári Ch.1-4
- **Policy Gradient:** Sutton & Barto Ch.13; Schulman et al.

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| — | `01-mdp/` | MDPs, Bellman equations, value/policy iteration, contraction mappings | planned |
| `Temporal-Difference-Learning` | `02-rl-algorithms/` | TD(0), n-step TD, TD(λ), SARSA, Q-learning, function approximation, deadly triad | **exists** |
| `Policy-Gradient-Theorem` | `03-policy-gradient/` | Policy gradient theorem, REINFORCE, baseline methods | **exists** |
| `Trust-Region-Policy-Optimization` | `03-policy-gradient/` | TRPO, natural policy gradient, KL-constrained optimization | **exists** |
| `Proximal-Policy-Optimization` | `03-policy-gradient/` | PPO, clipped surrogate objective, advantage estimation | **exists** |

## Prerequisites

- **Phase 01** (measure theory and probability foundations) — required for all documents in this phase

## Internal Reading Order

```
MDP (planned) → Temporal-Difference-Learning → Policy-Gradient-Theorem
  → Trust-Region-Policy-Optimization → Proximal-Policy-Optimization
```

This is a strict sequential chain — each document depends on all preceding ones.
