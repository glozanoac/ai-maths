# CLAUDE.md

## Project Overview
MARL predator-prey grid world: 2 predators catch 1 prey on a 7x7 grid. Compares IQL (tabular, independent) vs VDN (neural, cooperative).

## Key Commands
```bash
python train_random.py [--env env0|env1]   # baseline (~1K episodes)
python train_iql.py    [--env env0|env1]   # independent learning (~10K episodes)
python train_vdn.py    [--env env0|env1]   # cooperative learning (~5K episodes)
python evaluate.py     [--env env0|env1]   # compare all methods
python visualize.py --agent [random|iql|vdn] [--env env0|env1]  # pygame
python demo_ambush.py  [--env env0|env1] [--render]  # block-and-hunt demo
```

## Maps
- `env0` — Open 7x7 grid (default, no walls)
- `env1` — Room with single exit (3x3 interior, exit at (5,3)) for block-and-hunt scenarios

## Architecture
- `predator_prey/env/grid_world.py` — Core env with PettingZoo-style API + wall support
- `predator_prey/env/maps.py` — Map configurations (env0, env1)
- `predator_prey/env/renderer.py` — Pygame renderer (supports walls)
- `predator_prey/agents/iql_agent.py` — Tabular Q-learning (numpy only)
- `predator_prey/agents/vdn_agent.py` — Neural VDN (PyTorch)
- `predator_prey/utils/metrics.py` — Tracking and matplotlib plots
- Checkpoints saved to `checkpoints/`, plots to `results/`

## Conventions
- Reward modes: "individual" (IQL) or "cooperative" (VDN)
- Observations: 6D int vector [self_r, self_c, other_dr, other_dc, prey_dr, prey_dc]
- Actions: 0=UP, 1=DOWN, 2=LEFT, 3=RIGHT, 4=STAY
