# Phase 04 -- Deep Reinforcement Learning

Combines deep learning function approximation with reinforcement learning algorithms: value-based methods (DQN and extensions), policy-based methods with neural networks, and model-based approaches. This phase synthesizes Phases 02 and 03.

## Reference Textbooks

- **Value-Based:** Mnih et al. 2015 (DQN), Van Hasselt et al. 2016 (Double DQN), Wang et al. 2016 (Dueling), Bellemare et al. 2017 (C51)
- **Policy-Based:** Schulman et al. 2015 (TRPO), Schulman et al. 2017 (PPO), Lillicrap et al. 2016 (DDPG), Fujimoto et al. 2018 (TD3), Haarnoja et al. 2018 (SAC)
- **Model-Based:** Sutton 1991 (Dyna), Schrittwieser et al. 2020 (MuZero), Hafner et al. 2020 (Dreamer)

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| `01-dqn-and-extensions` | `01-value-based/` | DQN, experience replay, target networks, Double DQN, Dueling, overestimation bias | planned |
| `02-distributional-rl` | `01-value-based/` | C51, quantile regression DQN, IQN, distributional Bellman equation | planned |
| `01-trust-region-methods` | `02-policy-based/` | TRPO, natural policy gradient, KL-constrained optimization | **exists** |
| `02-proximal-policy-optimization` | `02-policy-based/` | PPO, clipped surrogate objective, advantage estimation | **exists** |
| `03-deterministic-policy-gradient` | `02-policy-based/` | Deterministic PG theorem, DDPG, TD3 | planned |
| `04-maximum-entropy-rl` | `02-policy-based/` | Maximum entropy framework, SAC, two-timescale actor-critic analysis | planned |
| `01-model-based-rl` | `03-model-based/` | Dyna, MuZero, Dreamer, world models, planning with learned models | planned |

## Prerequisites

- **Phase 02** (core RL theory) -- required for all documents
- **Phase 03** (deep learning foundations) -- required for all documents

## Internal Reading Order

```
01-dqn-and-extensions -> 02-distributional-rl
01-trust-region-methods -> 02-proximal-policy-optimization
03-deterministic-policy-gradient
04-maximum-entropy-rl
01-model-based-rl
```

Value-based and policy-based tracks can be read in parallel. Trust-region methods must precede PPO. Model-based methods are independent.
