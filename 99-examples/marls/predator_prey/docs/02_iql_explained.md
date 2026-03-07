# Independent Q-Learning (IQL)

## Q-Learning Refresher

Q-learning is a model-free RL algorithm that learns the optimal action-value function Q*(s, a) — the expected cumulative reward from taking action `a` in state `s` and then acting optimally.

The update rule:
```
Q(s, a) <- Q(s, a) + alpha * (r + gamma * max_a' Q(s', a') - Q(s, a))
```

Where:
- `alpha` (0.1): Learning rate — how much to update towards the new estimate
- `gamma` (0.99): Discount factor — how much to value future rewards
- `r`: Immediate reward
- `s'`: Next state

## IQL: Q-Learning with Multiple Agents

**Independent Q-Learning** is the simplest multi-agent approach: each agent runs its own Q-learning algorithm, treating other agents as part of the environment.

Each predator maintains its own Q-table mapping `(observation, action) -> Q-value`. From each agent's perspective, it's solving a single-agent problem — it doesn't know or care that the other predator is also learning.

### Implementation Details

- **Q-table**: Dictionary `{(obs_tuple): np.array(5)}` — one Q-value per action
- **State discretization**: Observations are clipped to [-3, +3] for relative positions, giving at most 7^6 = ~118K possible states per agent
- **Exploration**: Epsilon-greedy, decaying from 1.0 to 0.05 over 8,000 episodes
- **No neural networks**: Pure NumPy implementation

## The Non-Stationarity Problem

IQL has a fundamental issue in multi-agent settings: **the environment is non-stationary from each agent's perspective**.

When agent A updates its policy, the behavior of agent A changes. But agent B's Q-table was learned assuming agent A's old behavior. From B's perspective, the "environment" (which includes A) has changed. This violates a key assumption of Q-learning convergence — that the MDP is stationary.

In practice, IQL still works reasonably well in simple environments. But it can't learn truly coordinated strategies because neither agent explicitly reasons about the other's behavior.

## Expected Results

- IQL should significantly outperform random agents (40-70% capture rate vs ~5-15%)
- Each predator learns to chase the prey independently
- But they don't learn to coordinate — e.g., one predator cutting off escape routes while the other chases
- The capture rate plateaus below what coordinated agents can achieve
