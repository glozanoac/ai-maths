import numpy as np

from .base_agent import BaseAgent


class RandomAgent(BaseAgent):
    """Uniform random action selection baseline."""

    def __init__(self, n_actions=5):
        self.n_actions = n_actions

    def select_action(self, observation, explore=True):
        return np.random.randint(self.n_actions)

    def learn(self, *args, **kwargs):
        pass

    def save(self, path):
        pass

    def load(self, path):
        pass
