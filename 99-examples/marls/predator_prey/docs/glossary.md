# MARL Glossary

**Agent**: An entity that observes the environment and takes actions to maximize its cumulative reward.

**Action space**: The set of possible actions an agent can take. In our case: {UP, DOWN, LEFT, RIGHT, STAY}.

**CTDE (Centralized Training, Decentralized Execution)**: A paradigm where agents share information during training but act independently at test time. VDN uses this approach.

**Credit assignment**: The problem of determining which agent's actions contributed to a team reward. VDN addresses this through value decomposition.

**Discount factor (gamma)**: A value in [0, 1] that determines how much future rewards are worth relative to immediate rewards. gamma=0.99 means a reward 100 steps in the future is worth ~37% of an immediate reward.

**Epsilon-greedy**: An exploration strategy that takes a random action with probability epsilon and the greedy (best Q-value) action otherwise. Epsilon typically decays during training.

**Experience replay**: A buffer that stores past transitions (s, a, r, s', done) and samples random mini-batches for training. Breaks temporal correlations and improves sample efficiency.

**IGM (Individual-Global-Max)**: The property that the optimal joint action can be found by each agent independently maximizing its own value function. VDN satisfies IGM by construction.

**IQL (Independent Q-Learning)**: Each agent runs its own Q-learning independently, treating other agents as part of the environment.

**Joint action**: The combined actions of all agents at a single timestep. In our case: (action_pred0, action_pred1).

**MARL (Multi-Agent Reinforcement Learning)**: RL with multiple learning agents in a shared environment.

**Non-stationarity**: In MARL, the environment appears non-stationary to each agent because other agents are simultaneously changing their policies.

**Observation**: What an individual agent can see. May differ from the global state. In our case: [self_pos, relative_other_pred, relative_prey].

**Q-value / Q-function**: Q(s, a) estimates the expected cumulative reward from taking action a in state s and then following the optimal policy.

**Reward shaping**: Designing the reward function to guide learning toward desired behavior. Our cooperative bonus (+25 for coordinated capture) is a form of reward shaping.

**State**: The complete description of the environment at a timestep. In our case: all agent positions.

**Target network**: A slowly-updated copy of the Q-network used to compute stable training targets. Prevents the "moving target" problem in deep Q-learning.

**VDN (Value Decomposition Network)**: Decomposes the team Q-value as the sum of individual agent Q-values: Q_total = Q_1 + Q_2. Enables CTDE.

**QMIX**: An extension of VDN that uses a monotonic mixing network instead of simple summation, allowing more expressive value decomposition while still satisfying IGM.
