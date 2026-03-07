import pickle
import numpy as np
from collections import defaultdict

from .base_agent import BaseAgent


class IQLAgent(BaseAgent):
    """Tabular Independent Q-Learning agent.

    Each agent maintains its own Q-table mapping (observation, action) -> Q-value.
    Observations are discretized by clipping relative positions to [-3, +3].
    """

    def __init__(self, n_actions=5, alpha=0.1, gamma=0.99,
                 epsilon_start=1.0, epsilon_end=0.05, epsilon_decay_steps=8000):
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon_start = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay_steps = epsilon_decay_steps
        self.q_table = defaultdict(lambda: np.zeros(n_actions))
        self._step_count = 0

    @property
    def epsilon(self):
        frac = min(1.0, self._step_count / self.epsilon_decay_steps)
        return self.epsilon_start + frac * (self.epsilon_end - self.epsilon_start)

    def _obs_to_key(self, obs):
        """Convert observation to hashable key, clipping relative coords to [-3, 3]."""
        clipped = obs.copy()
        # Indices 2-5 are relative positions
        clipped[2:] = np.clip(clipped[2:], -3, 3)
        return tuple(clipped)

    def select_action(self, observation, explore=True):
        if explore and np.random.random() < self.epsilon:
            return np.random.randint(self.n_actions)
        key = self._obs_to_key(observation)
        q_values = self.q_table[key]
        # Break ties randomly
        max_q = np.max(q_values)
        best_actions = np.where(q_values == max_q)[0]
        return np.random.choice(best_actions)

    def learn(self, obs, action, reward, next_obs, done):
        key = self._obs_to_key(obs)
        next_key = self._obs_to_key(next_obs)

        target = reward
        if not done:
            target += self.gamma * np.max(self.q_table[next_key])

        self.q_table[key][action] += self.alpha * (target - self.q_table[key][action])
        self._step_count += 1

    def save(self, path):
        data = {
            "q_table": dict(self.q_table),
            "step_count": self._step_count,
        }
        with open(path, "wb") as f:
            pickle.dump(data, f)

    def load(self, path):
        with open(path, "rb") as f:
            data = pickle.load(f)
        self.q_table = defaultdict(lambda: np.zeros(self.n_actions))
        self.q_table.update(data["q_table"])
        self._step_count = data["step_count"]
