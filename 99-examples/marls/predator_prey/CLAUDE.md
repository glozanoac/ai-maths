# CLAUDE.md

## Project Overview
MARL predator-prey grid world: 2 predators catch 1 prey on a 7x7 grid. Compares IQL (tabular, independent) vs VDN (neural, cooperative).

## Key Commands
```bash
source env/bin/activate
python train_random.py   # baseline (~1K episodes)
python train_iql.py      # independent learning (~10K episodes)
python train_vdn.py      # cooperative learning (~5K episodes)
python evaluate.py       # compare all methods
python visualize.py --agent [random|iql|vdn]  # pygame visualization
```

## Architecture
- `predator_prey/env/grid_world.py` — Core env with PettingZoo-style API
- `predator_prey/agents/iql_agent.py` — Tabular Q-learning (numpy only)
- `predator_prey/agents/vdn_agent.py` — Neural VDN (PyTorch)
- `predator_prey/utils/metrics.py` — Tracking and matplotlib plots
- Checkpoints saved to `checkpoints/`, plots to `results/`

## Conventions
- Reward modes: "individual" (IQL) or "cooperative" (VDN)
- Observations: 6D int vector [self_r, self_c, other_dr, other_dc, prey_dr, prey_dc]
- Actions: 0=UP, 1=DOWN, 2=LEFT, 3=RIGHT, 4=STAY
