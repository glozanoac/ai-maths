from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Abstract base class for all agents."""

    @abstractmethod
    def select_action(self, observation, explore=True):
        """Select an action given an observation."""

    @abstractmethod
    def learn(self, *args, **kwargs):
        """Update the agent's policy from experience."""

    @abstractmethod
    def save(self, path):
        """Save the agent's learned parameters."""

    @abstractmethod
    def load(self, path):
        """Load previously saved parameters."""
