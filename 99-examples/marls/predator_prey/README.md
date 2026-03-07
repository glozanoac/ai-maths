# Predator-Prey: Multi-Agent Reinforcement Learning

A learning-focused MARL project comparing independent vs cooperative strategies in a predator-prey grid world.

**2 predators** must coordinate to catch **1 prey** on a 7x7 grid. We compare:
- **IQL** (Independent Q-Learning) — each predator learns independently
- **VDN** (Value Decomposition Network) — predators learn cooperatively via shared team reward

## Setup

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Quick Start

```bash
# 1. Verify environment works with random agents
python train_random.py

# 2. Train independent Q-learning agents (10K episodes)
python train_iql.py

# 3. Train cooperative VDN agents (5K episodes)
python train_vdn.py

# 4. Compare all methods
python evaluate.py

# 5. Watch agents play (requires display)
python visualize.py --agent vdn
```

## Project Structure

```
train_random.py         # Sanity check baseline
train_iql.py            # Train independent Q-learning
train_vdn.py            # Train cooperative VDN
evaluate.py             # Compare all methods
visualize.py            # Watch agents play (pygame)
predator_prey/
  env/
    grid_world.py       # Core environment (7x7 grid, 2 predators, 1 prey)
    renderer.py         # Pygame visualization
  agents/
    base_agent.py       # Abstract agent interface
    random_agent.py     # Random baseline
    iql_agent.py        # Tabular Independent Q-Learning
    vdn_agent.py        # Value Decomposition Network (PyTorch)
  utils/
    replay_buffer.py    # Experience replay for VDN
    metrics.py          # Training metrics and plotting
docs/                   # Detailed explanations of each component
notebooks/              # Interactive exploration
```

## Expected Results

| Method | Capture Rate | Cooperative Captures |
|--------|-------------|---------------------|
| Random | ~5-15%      | Rare                |
| IQL    | ~40-70%     | Accidental          |
| VDN    | ~60-90%     | Frequent            |

## Documentation

- [Environment Design](docs/01_environment_design.md) — Grid world design decisions
- [IQL Explained](docs/02_iql_explained.md) — Independent Q-Learning and non-stationarity
- [VDN Explained](docs/03_vdn_explained.md) — Value decomposition and CTDE
- [Comparing Results](docs/04_comparing_results.md) — How to interpret training curves
- [Glossary](docs/glossary.md) — MARL terminology reference
