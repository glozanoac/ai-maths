# Phase 06 — Aerospace Applications

Applies deep RL and multi-agent methods to aerospace domains: continuous control on Lie groups, safety-constrained learning, partial observability, simulation-to-reality transfer, and multi-vehicle coordination.

## Reference Textbooks

- **Continuous Control:** Lillicrap et al. (DDPG), Lie group methods literature
- **Safety:** Altman (constrained MDPs), Chow et al. (Lyapunov-based methods)
- **Partial Observability:** Kaelbling et al. (POMDPs), belief-space planning literature
- **Sim-to-Real:** Tobin et al. (domain randomization), system identification literature
- **Multi-Vehicle:** formation control and task allocation literature

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| — | `01-continuous-control/` | Continuous action spaces, Lie group methods | planned |
| — | `02-safety/` | Constrained MDPs, Lyapunov-based methods | planned |
| — | `03-partial-observability/` | POMDPs, belief-space planning | planned |
| — | `04-sim-to-real/` | Domain randomization, system identification | planned |
| — | `05-multi-vehicle/` | Formation control, task allocation | planned |

## Prerequisites

- **Phase 04** (deep RL) — required for all documents
- **Phase 05** (MARL) — required for multi-vehicle coordination, beneficial for all

## Internal Reading Order

```
continuous-control → safety → partial-observability → sim-to-real → multi-vehicle
```

Continuous control establishes the action-space framework; safety adds constraints; partial observability and sim-to-real address deployment challenges; multi-vehicle brings in multi-agent coordination.
