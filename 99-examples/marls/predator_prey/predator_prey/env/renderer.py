import numpy as np

try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False


class Renderer:
    """Pygame-based grid renderer for the Predator-Prey environment."""

    CELL_SIZE = 80
    COLORS = {
        "bg": (255, 255, 255),
        "grid": (200, 200, 200),
        "predator": (220, 50, 50),
        "prey": (50, 50, 220),
        "capture": (180, 50, 180),
        "wall": (60, 60, 60),
    }

    def __init__(self, grid_size, cell_size=80):
        if not PYGAME_AVAILABLE:
            raise ImportError("pygame is required for rendering. Install with: pip install pygame")
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.window_size = grid_size * cell_size
        self.screen = None
        self.clock = None

    def init(self):
        pygame.init()
        header_height = 40
        self.header_height = header_height
        self.screen = pygame.display.set_mode((self.window_size, self.window_size + header_height))
        pygame.display.set_caption("Predator-Prey")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 18, bold=True)
        self.header_font = pygame.font.SysFont("monospace", 22, bold=True)

    def _cell_center(self, r, c):
        cx = c * self.cell_size + self.cell_size // 2
        cy = r * self.cell_size + self.cell_size // 2 + self.header_height
        return cx, cy

    def render_frame(self, frame_data, fps=5, episode=None, total_episodes=None):
        """Render a single frame. frame_data is a dict with 'predators', 'prey', 'step'.
        Returns False if window was closed."""
        if self.screen is None:
            self.init()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
                return False

        self.screen.fill(self.COLORS["bg"])

        predators = frame_data["predators"]
        prey = frame_data["prey"]
        step = frame_data["step"]

        # Draw header with episode and step counter
        ep_str = f"Ep: {episode}/{total_episodes}  " if episode is not None else ""
        header_text = self.header_font.render(f"{ep_str}Step: {step}", True, (30, 30, 30))
        self.screen.blit(header_text, (10, 8))

        # Draw legend in header
        legend_x = self.window_size - 280
        pygame.draw.circle(self.screen, self.COLORS["predator"], (legend_x, 20), 8)
        leg1 = self.font.render("Predator", True, (30, 30, 30))
        self.screen.blit(leg1, (legend_x + 14, 10))
        pygame.draw.circle(self.screen, self.COLORS["prey"], (legend_x + 130, 20), 8)
        leg2 = self.font.render("Prey", True, (30, 30, 30))
        self.screen.blit(leg2, (legend_x + 144, 10))

        # Draw grid lines
        for i in range(self.grid_size + 1):
            y_off = self.header_height
            pygame.draw.line(self.screen, self.COLORS["grid"],
                             (i * self.cell_size, y_off),
                             (i * self.cell_size, self.window_size + y_off))
            pygame.draw.line(self.screen, self.COLORS["grid"],
                             (0, i * self.cell_size + y_off),
                             (self.window_size, i * self.cell_size + y_off))

        # Draw walls
        walls = frame_data.get("walls", set())
        for wr, wc in walls:
            rect = pygame.Rect(
                wc * self.cell_size, wr * self.cell_size + self.header_height,
                self.cell_size, self.cell_size,
            )
            pygame.draw.rect(self.screen, self.COLORS["wall"], rect)

        radius = self.cell_size // 3
        label_color = (255, 255, 255)

        # Draw prey
        pr, pc = prey
        cx, cy = self._cell_center(pr, pc)
        captured = any(tuple(p) == prey for p in predators)
        if captured:
            pygame.draw.circle(self.screen, self.COLORS["capture"], (cx, cy), radius)
        else:
            pygame.draw.circle(self.screen, self.COLORS["prey"], (cx, cy), radius)
        label = self.font.render("Prey", True, label_color)
        lr = label.get_rect(center=(cx, cy))
        self.screen.blit(label, lr)

        # Draw predators
        for i, (pr, pc) in enumerate(predators):
            cx, cy = self._cell_center(pr, pc)
            # Offset slightly if both predators on same cell
            if i == 1 and predators[0] == predators[1]:
                cy += radius + 5
            pygame.draw.circle(self.screen, self.COLORS["predator"], (cx, cy), radius)
            label = self.font.render(f"P{i}", True, label_color)
            lr = label.get_rect(center=(cx, cy))
            self.screen.blit(label, lr)

        pygame.display.flip()
        self.clock.tick(fps)
        return True

    def render_episode(self, frames, fps=5, episode=None, total_episodes=None):
        """Render a sequence of frame dicts."""
        for frame in frames:
            if not self.render_frame(frame, fps, episode=episode, total_episodes=total_episodes):
                break

    def close(self):
        if self.screen is not None:
            pygame.quit()
            self.screen = None

    @staticmethod
    def save_frames(frames, path):
        """Save frames as numpy array for post-hoc review."""
        np.save(path, np.array(frames))
