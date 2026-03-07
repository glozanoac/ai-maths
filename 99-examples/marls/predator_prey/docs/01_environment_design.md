# Environment Design

## Why a Grid World?

Grid worlds are the standard starting point for reinforcement learning research. They offer:
- **Discrete state/action spaces** that are easy to reason about
- **Visual interpretability** — you can see what the agents are doing
- **Tractable for tabular methods** — no neural networks needed for basic approaches
- **Fast simulation** — thousands of episodes per second

## Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Grid size | 7x7 | Small enough for tabular Q-learning (~118K states with clipping), large enough that coordination matters |
| Predators | 2 | Minimum to demonstrate multi-agent coordination |
| Prey | 1 | Keeps focus on predator learning, not predator-prey co-evolution |
| Prey policy | Rule-based (flee + 20% random) | Deterministic fleeing would be too predictable; randomness prevents trivial solutions |
| Max steps | 100 | ~2x the grid diameter, prevents infinite episodes |

## Observation Space

Each predator receives a 6D integer vector:
```
[self_row, self_col, other_pred_delta_row, other_pred_delta_col, prey_delta_row, prey_delta_col]
```

Using relative positions (deltas) for the other predator and prey makes the representation partially translation-invariant — the agent doesn't need to learn separate policies for every absolute position on the grid.

For IQL, relative positions are clipped to [-3, +3] to keep the Q-table manageable.

## Action Space

5 discrete actions: UP, DOWN, LEFT, RIGHT, STAY. All agents act simultaneously. Actions that would move an agent off the grid are clipped (the agent stays at the edge).

## Reward Structure

### Individual mode (for IQL)
- **-0.1 per step**: Encourages efficient capture
- **+10 on capture**: Any predator occupying the prey's cell

### Cooperative mode (for VDN)
- **-0.1 per step**: Same time pressure
- **+10 on capture**: Base capture reward
- **+25 on cooperative capture**: Both predators adjacent to (or on top of) the prey when captured. This bonus incentivizes surrounding behavior.

## Capture Condition

A predator captures the prey by occupying the same cell. The episode ends immediately on capture or after `max_steps` timesteps (timeout).

## Prey Behavior

The prey uses a simple rule-based policy:
1. Find the nearest predator (Manhattan distance)
2. Try all 5 actions and pick the one that maximizes distance from the nearest predator
3. With 20% probability, take a random action instead

The randomness prevents the prey from being fully predictable, which would make the problem too easy. It also prevents deterministic oscillation patterns.
