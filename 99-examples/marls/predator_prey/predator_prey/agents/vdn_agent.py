import os
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from .base_agent import BaseAgent


class QNetwork(nn.Module):
    """Per-agent Q-network: 6 -> 64 -> 64 -> 5."""

    def __init__(self, obs_dim=6, n_actions=5, hidden_dim=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(obs_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, n_actions),
        )

    def forward(self, x):
        return self.net(x)


class VDNAgent(BaseAgent):
    """Value Decomposition Network agent for cooperative multi-agent learning.

    Two per-agent Q-networks whose outputs are summed to form Q_total.
    Trained end-to-end with shared replay buffer and target networks.
    """

    def __init__(self, n_agents=2, obs_dim=6, n_actions=5,
                 lr=0.001, gamma=0.99, tau=0.005, batch_size=32,
                 epsilon_start=1.0, epsilon_end=0.05, epsilon_decay_steps=5000):
        self.n_agents = n_agents
        self.n_actions = n_actions
        self.gamma = gamma
        self.tau = tau
        self.batch_size = batch_size
        self.epsilon_start = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay_steps = epsilon_decay_steps
        self._step_count = 0

        self.device = torch.device("cpu")

        # Per-agent online and target networks
        self.q_networks = [QNetwork(obs_dim, n_actions).to(self.device) for _ in range(n_agents)]
        self.target_networks = [QNetwork(obs_dim, n_actions).to(self.device) for _ in range(n_agents)]
        for i in range(n_agents):
            self.target_networks[i].load_state_dict(self.q_networks[i].state_dict())

        # Single optimizer for all agent networks
        all_params = []
        for net in self.q_networks:
            all_params.extend(net.parameters())
        self.optimizer = optim.Adam(all_params, lr=lr)

    @property
    def epsilon(self):
        frac = min(1.0, self._step_count / self.epsilon_decay_steps)
        return self.epsilon_start + frac * (self.epsilon_end - self.epsilon_start)

    def select_action(self, observation, agent_idx=0, explore=True):
        if explore and np.random.random() < self.epsilon:
            return np.random.randint(self.n_actions)

        obs_tensor = torch.FloatTensor(observation).unsqueeze(0).to(self.device)
        with torch.no_grad():
            q_values = self.q_networks[agent_idx](obs_tensor)
        return q_values.argmax(dim=1).item()

    def learn(self, replay_buffer):
        """Update all agent networks using a batch from the replay buffer."""
        if len(replay_buffer) < self.batch_size:
            return None

        batch = replay_buffer.sample(self.batch_size)
        obs_batch, action_batch, reward_batch, next_obs_batch, done_batch = batch

        # obs_batch shape: (batch, n_agents, obs_dim)
        # action_batch shape: (batch, n_agents)
        # reward_batch shape: (batch,) — team reward
        # done_batch shape: (batch,)

        obs_batch = torch.FloatTensor(obs_batch).to(self.device)
        action_batch = torch.LongTensor(action_batch).to(self.device)
        reward_batch = torch.FloatTensor(reward_batch).to(self.device)
        next_obs_batch = torch.FloatTensor(next_obs_batch).to(self.device)
        done_batch = torch.FloatTensor(done_batch).to(self.device)

        # Compute Q_total = sum of individual Q(s_i, a_i)
        q_total = torch.zeros(self.batch_size, device=self.device)
        for i in range(self.n_agents):
            q_values = self.q_networks[i](obs_batch[:, i])
            q_taken = q_values.gather(1, action_batch[:, i].unsqueeze(1)).squeeze(1)
            q_total += q_taken

        # Compute target Q_total
        with torch.no_grad():
            target_q_total = torch.zeros(self.batch_size, device=self.device)
            for i in range(self.n_agents):
                target_q = self.target_networks[i](next_obs_batch[:, i])
                target_q_total += target_q.max(dim=1)[0]

        target = reward_batch + self.gamma * target_q_total * (1 - done_batch)

        loss = nn.functional.mse_loss(q_total, target)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # Soft update target networks
        for i in range(self.n_agents):
            for param, target_param in zip(self.q_networks[i].parameters(),
                                           self.target_networks[i].parameters()):
                target_param.data.copy_(self.tau * param.data + (1 - self.tau) * target_param.data)

        self._step_count += 1
        return loss.item()

    def save(self, path):
        os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
        data = {
            "q_networks": [net.state_dict() for net in self.q_networks],
            "target_networks": [net.state_dict() for net in self.target_networks],
            "step_count": self._step_count,
        }
        torch.save(data, path)

    def load(self, path):
        data = torch.load(path, map_location=self.device, weights_only=True)
        for i in range(self.n_agents):
            self.q_networks[i].load_state_dict(data["q_networks"][i])
            self.target_networks[i].load_state_dict(data["target_networks"][i])
        self._step_count = data["step_count"]
