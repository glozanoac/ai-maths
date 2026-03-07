import numpy as np


# Actions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
STAY = 4

ACTION_DELTAS = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1),
    STAY: (0, 0),
}

AGENT_NAMES = ["predator_0", "predator_1"]


class PredatorPreyEnv:
    """7x7 grid world with 2 predators and 1 rule-based prey."""

    def __init__(self, grid_size=7, max_steps=100, reward_mode="individual",
                 walls=None):
        self.grid_size = grid_size
        self.max_steps = max_steps
        self.reward_mode = reward_mode  # "individual" or "cooperative"
        self.walls = set(walls) if walls else set()  # set of (r, c) tuples
        self.n_actions = 5
        self.agents = AGENT_NAMES

        self._pred_positions = None
        self._prey_position = None
        self._step_count = 0

    def reset(self, seed=None):
        if seed is not None:
            self._rng = np.random.RandomState(seed)
        else:
            self._rng = np.random.RandomState()

        # Place agents at random non-overlapping positions (not on walls)
        positions = []
        while len(positions) < 3:
            pos = (self._rng.randint(self.grid_size), self._rng.randint(self.grid_size))
            if pos not in positions and pos not in self.walls:
                positions.append(pos)

        self._pred_positions = [list(positions[0]), list(positions[1])]
        self._prey_position = list(positions[2])
        self._step_count = 0

        return self._get_observations()

    def step(self, actions):
        self._step_count += 1

        # Move predators
        for i, agent in enumerate(self.agents):
            action = actions[agent]
            dr, dc = ACTION_DELTAS[action]
            new_r = int(np.clip(self._pred_positions[i][0] + dr, 0, self.grid_size - 1))
            new_c = int(np.clip(self._pred_positions[i][1] + dc, 0, self.grid_size - 1))
            if (new_r, new_c) not in self.walls:
                self._pred_positions[i] = [new_r, new_c]

        # Move prey (rule-based: flee from nearest predator)
        self._move_prey()

        # Check capture
        captured = False
        capturing_predators = []
        for i in range(2):
            if self._pred_positions[i] == self._prey_position:
                captured = True
                capturing_predators.append(i)

        # Check if both predators are adjacent to prey at capture
        both_adjacent = False
        if captured:
            for i in range(2):
                if i not in capturing_predators:
                    dist = abs(self._pred_positions[i][0] - self._prey_position[0]) + \
                           abs(self._pred_positions[i][1] - self._prey_position[1])
                    if dist <= 1:
                        both_adjacent = True

        # Compute rewards
        rewards = {}
        for agent in self.agents:
            if captured:
                rewards[agent] = 10.0
                if self.reward_mode == "cooperative" and both_adjacent:
                    rewards[agent] = 25.0
            else:
                rewards[agent] = -0.1

        done = captured or self._step_count >= self.max_steps
        dones = {agent: done for agent in self.agents}
        dones["__all__"] = done

        infos = {
            "captured": captured,
            "cooperative_capture": captured and both_adjacent,
            "step": self._step_count,
        }

        return self._get_observations(), rewards, dones, infos

    def _move_prey(self):
        """Rule-based prey: move away from the nearest predator."""
        prey_r, prey_c = self._prey_position

        # Find nearest predator
        min_dist = float("inf")
        nearest_pred = None
        for pos in self._pred_positions:
            dist = abs(pos[0] - prey_r) + abs(pos[1] - prey_c)
            if dist < min_dist:
                min_dist = dist
                nearest_pred = pos

        # Try to maximize distance from nearest predator
        best_action = STAY
        best_dist = min_dist

        for action in range(5):
            dr, dc = ACTION_DELTAS[action]
            new_r = int(np.clip(prey_r + dr, 0, self.grid_size - 1))
            new_c = int(np.clip(prey_c + dc, 0, self.grid_size - 1))
            if (new_r, new_c) in self.walls:
                continue
            dist = abs(nearest_pred[0] - new_r) + abs(nearest_pred[1] - new_c)
            if dist > best_dist:
                best_dist = dist
                best_action = action

        # Add randomness: 20% chance of random action
        if self._rng.random() < 0.2:
            action = self._rng.randint(5)
            dr, dc = ACTION_DELTAS[action]
            nr = int(np.clip(prey_r + dr, 0, self.grid_size - 1))
            nc = int(np.clip(prey_c + dc, 0, self.grid_size - 1))
            if (nr, nc) not in self.walls:
                best_action = action

        dr, dc = ACTION_DELTAS[best_action]
        self._prey_position[0] = int(np.clip(prey_r + dr, 0, self.grid_size - 1))
        self._prey_position[1] = int(np.clip(prey_c + dc, 0, self.grid_size - 1))

    def _get_observations(self):
        """Per-predator observation: [self_x, self_y, other_pred_dx, other_pred_dy, prey_dx, prey_dy]."""
        obs = {}
        for i, agent in enumerate(self.agents):
            other_i = 1 - i
            self_pos = self._pred_positions[i]
            other_pos = self._pred_positions[other_i]
            prey_pos = self._prey_position

            obs[agent] = np.array([
                self_pos[0], self_pos[1],
                other_pos[0] - self_pos[0], other_pos[1] - self_pos[1],
                prey_pos[0] - self_pos[0], prey_pos[1] - self_pos[1],
            ], dtype=np.int32)

        return obs

    def get_positions(self):
        """Return agent positions for rendering with labels."""
        return {
            "predators": [tuple(p) for p in self._pred_positions],
            "prey": tuple(self._prey_position),
            "step": self._step_count,
            "walls": self.walls,
        }

    def get_state(self):
        """Global state for centralized training: all positions concatenated."""
        return np.array(
            self._pred_positions[0] + self._pred_positions[1] + self._prey_position,
            dtype=np.int32,
        )

    def render(self):
        """Return grid as numpy array for the renderer."""
        grid = np.zeros((self.grid_size, self.grid_size), dtype=np.int32)
        # 1 = predator, 2 = prey, 3 = both (capture), 4 = wall
        for r, c in self.walls:
            grid[r, c] = 4
        for pos in self._pred_positions:
            grid[pos[0], pos[1]] = 1
        pr, pc = self._prey_position
        if grid[pr, pc] == 1:
            grid[pr, pc] = 3
        else:
            grid[pr, pc] = 2
        return grid
