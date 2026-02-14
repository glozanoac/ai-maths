# Phase 04 -- Deep Reinforcement Learning

Combines deep learning function approximation with reinforcement learning algorithms: value-based methods (DQN and extensions), policy-based methods with neural networks, and model-based approaches. This phase synthesizes Phases 02 and 03.

## Reference Textbooks

- **Value-Based:** Mnih et al. (DQN), Hessel et al. (Rainbow), Bellemare et al. (distributional RL)
- **Policy-Based:** Mnih et al. (A3C), Schulman et al. (PPO), Haarnoja et al. (SAC)
- **Model-Based:** Sutton (Dyna), Schrittwieser et al. (MuZero), Ha & Schmidhuber (world models)

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| -- | `01-value-based/` | DQN, Rainbow, distributional RL | planned |
| -- | `02-policy-based/` | A3C, PPO+function approximation, SAC | planned |
| -- | `03-model-based/` | Dyna, MuZero, world models | planned |

## Prerequisites

- **Phase 02** (core RL theory) -- required for all documents
- **Phase 03** (deep learning foundations) -- required for all documents

## Internal Reading Order

```
value-based -> policy-based -> model-based
```

Value-based methods introduce deep function approximation in RL; policy-based methods build on this; model-based methods extend both.
