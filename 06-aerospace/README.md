# Phase 06 -- Aerospace Applications

Applies deep RL and multi-agent methods to aerospace domains: continuous control on Lie groups, safety-constrained learning, partial observability, simulation-to-reality transfer, and multi-vehicle coordination.

## Reference Textbooks

- **Continuous Control:** Lillicrap et al. (DDPG), hierarchical RL and MPC+RL literature
- **Safety:** Altman 1999 (constrained MDPs), Achiam 2017 (CPO), Chow et al. 2018 (Lyapunov)
- **Partial Observability:** Krishnamurthy Ch.1-5, 7-8; Kaelbling et al. (POMDPs)
- **Sim-to-Real:** Tobin et al. 2017, Peng et al. 2018, Akkaya et al. 2019
- **Multi-Vehicle:** Sartoretti et al. 2019, Khan et al. 2020, Riviere et al. 2020

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| `01-continuous-control` | `01-continuous-control/` | High-dimensional action spaces, hierarchical RL, MPC+RL hybrids | planned |
| `01-safety-and-constraints` | `02-safety/` | Constrained MDPs, Lagrangian relaxation, CPO, Lyapunov stability, reachability | planned |
| `01-pomdps` | `03-partial-observability/` | POMDP formulation, belief states, structural results, approximate methods | planned |
| `01-sim-to-real-transfer` | `04-sim-to-real/` | Domain randomization, system identification, progressive nets | planned |
| `01-multi-vehicle-coordination` | `05-multi-vehicle/` | Formation control (graph Laplacian), collision avoidance, communication-aware coordination | planned |

## Prerequisites

- **Phase 04** (deep RL) -- required for all documents
- **Phase 05** (MARL) -- required for multi-vehicle coordination, beneficial for all

## Internal Reading Order

```
{continuous-control, safety, partial-observability, sim-to-real, multi-vehicle}
```

These topics are largely independent and can be read in any order, though continuous control provides useful context for all others.
