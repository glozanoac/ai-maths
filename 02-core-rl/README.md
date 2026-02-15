# Phase 02 -- Core Reinforcement Learning Theory

Formal development of reinforcement learning from first principles: Markov decision processes, temporal-difference methods, and policy gradient algorithms. Each document builds directly on its predecessor, forming a strict linear chain.

## Reference Textbooks

- **MDPs:** Puterman Ch.2-6, 8; Bertsekas & Tsitsiklis Ch.1-4
- **RL Algorithms:** Sutton & Barto (full); Szepesvari Ch.1-4
- **Policy Gradient:** Sutton & Barto Ch.13; Sutton et al. 2000, Kakade 2002

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| `01-mdp-formulation-and-finite-horizon` | `01-mdp/` | MDP model, policies, finite-horizon MDPs, backward induction | planned |
| `02-infinite-horizon-and-dynamic-programming` | `01-mdp/` | Discounted/average reward, Bellman equations, contraction, value/policy iteration, LP formulation | planned |
| `lesson-47-td0-and-nstep-td` | `02-rl-algorithms/` | MC baseline, TD(0) update, TD error properties, convergence of TD(0) via SA, bias-variance analysis, n-step returns, n-step TD convergence | **exists** |
| `lesson-48-td-lambda-eligibility-traces` | `02-rl-algorithms/` | Lambda-return (forward view), special cases, lambda-return decomposition, eligibility traces (backward view), forward-backward equivalence, trace variants | **exists** |
| `policy-gradient-theorem` | `03-policy-gradient/` | Policy gradient theorem, REINFORCE, baseline variance reduction, natural gradient, Fisher information | **exists** |

## Prerequisites

- **Phase 01** (measure theory, probability foundations, optimization) -- required for all documents in this phase

## Internal Reading Order

```
01-mdp-formulation (planned) -> 02-infinite-horizon-and-dp (planned)
  -> lesson-47-td0-and-nstep-td -> lesson-48-td-lambda-eligibility-traces
  -> policy-gradient-theorem
```

This is a strict sequential chain -- each document depends on all preceding ones. Policy gradient theorem leads into Phase 04 (trust-region and proximal methods).
