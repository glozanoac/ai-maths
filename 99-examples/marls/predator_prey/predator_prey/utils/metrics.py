import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


class MetricsTracker:
    """Track and plot training metrics."""

    def __init__(self):
        self.episode_returns = []
        self.episode_lengths = []
        self.captures = []
        self.cooperative_captures = []

    def record(self, total_return, length, captured, cooperative):
        self.episode_returns.append(total_return)
        self.episode_lengths.append(length)
        self.captures.append(float(captured))
        self.cooperative_captures.append(float(cooperative))

    def summary(self, last_n=100):
        if not self.episode_returns:
            return {}
        n = min(last_n, len(self.episode_returns))
        return {
            "mean_return": np.mean(self.episode_returns[-n:]),
            "mean_length": np.mean(self.episode_lengths[-n:]),
            "capture_rate": np.mean(self.captures[-n:]),
            "coop_capture_rate": np.mean(self.cooperative_captures[-n:]),
        }

    def plot(self, save_path, title="Training Progress", window=100):
        os.makedirs(os.path.dirname(save_path) if os.path.dirname(save_path) else ".", exist_ok=True)
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle(title)

        data = [
            (self.episode_returns, "Episode Return"),
            (self.episode_lengths, "Episode Length"),
            (self.captures, "Capture Rate"),
            (self.cooperative_captures, "Cooperative Capture Rate"),
        ]

        for ax, (values, label) in zip(axes.flat, data):
            ax.plot(values, alpha=0.3, color="blue")
            if len(values) >= window:
                rolling = np.convolve(values, np.ones(window) / window, mode="valid")
                ax.plot(range(window - 1, len(values)), rolling, color="red", linewidth=2)
            ax.set_xlabel("Episode")
            ax.set_ylabel(label)
            ax.set_title(label)

        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
        plt.close()

    @staticmethod
    def compare_plot(trackers, labels, save_path, window=100):
        """Plot comparison of multiple training runs."""
        os.makedirs(os.path.dirname(save_path) if os.path.dirname(save_path) else ".", exist_ok=True)
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

        for ax, (attr, title) in zip(axes, [("captures", "Capture Rate"), ("episode_returns", "Episode Return")]):
            for tracker, label, color in zip(trackers, labels, colors):
                values = getattr(tracker, attr)
                if len(values) >= window:
                    rolling = np.convolve(values, np.ones(window) / window, mode="valid")
                    ax.plot(range(window - 1, len(values)), rolling, label=label, color=color, linewidth=2)
            ax.set_xlabel("Episode")
            ax.set_ylabel(title)
            ax.set_title(title)
            ax.legend()

        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
        plt.close()
