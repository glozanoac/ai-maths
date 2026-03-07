import numpy as np


class ReplayBuffer:
    """Experience replay buffer for VDN training.

    Stores joint transitions: (obs_all_agents, actions_all, team_reward, next_obs_all, done).
    """

    def __init__(self, capacity=50000, n_agents=2, obs_dim=6):
        self.capacity = capacity
        self.n_agents = n_agents
        self.obs_dim = obs_dim
        self.pos = 0
        self.size = 0

        self.obs = np.zeros((capacity, n_agents, obs_dim), dtype=np.float32)
        self.actions = np.zeros((capacity, n_agents), dtype=np.int64)
        self.rewards = np.zeros(capacity, dtype=np.float32)
        self.next_obs = np.zeros((capacity, n_agents, obs_dim), dtype=np.float32)
        self.dones = np.zeros(capacity, dtype=np.float32)

    def push(self, obs, actions, reward, next_obs, done):
        """Store a joint transition.

        Args:
            obs: array of shape (n_agents, obs_dim)
            actions: array of shape (n_agents,)
            reward: float (team reward)
            next_obs: array of shape (n_agents, obs_dim)
            done: bool
        """
        self.obs[self.pos] = obs
        self.actions[self.pos] = actions
        self.rewards[self.pos] = reward
        self.next_obs[self.pos] = next_obs
        self.dones[self.pos] = float(done)

        self.pos = (self.pos + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def sample(self, batch_size):
        indices = np.random.randint(0, self.size, size=batch_size)
        return (
            self.obs[indices],
            self.actions[indices],
            self.rewards[indices],
            self.next_obs[indices],
            self.dones[indices],
        )

    def __len__(self):
        return self.size
