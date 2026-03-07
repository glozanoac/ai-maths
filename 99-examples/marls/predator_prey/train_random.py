"""Sanity check: run random agents to establish baseline capture rate."""

import argparse
import os

from tqdm import trange

from predator_prey.env import PredatorPreyEnv, MAPS
from predator_prey.agents import RandomAgent
from predator_prey.utils import MetricsTracker


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", choices=list(MAPS.keys()), default="env0")
    args = parser.parse_args()

    env = PredatorPreyEnv(walls=MAPS[args.env]["walls"])
    agents = {name: RandomAgent() for name in env.agents}
    metrics = MetricsTracker()
    n_episodes = 1000

    for ep in trange(n_episodes, desc="Random"):
        obs = env.reset()
        episode_return = 0
        done = False

        while not done:
            actions = {name: agents[name].select_action(obs[name]) for name in env.agents}
            next_obs, rewards, dones, infos = env.step(actions)
            episode_return += sum(rewards.values()) / len(env.agents)
            obs = next_obs
            done = dones["__all__"]

        metrics.record(episode_return, infos["step"], infos["captured"], infos["cooperative_capture"])

    summary = metrics.summary()
    print(f"\nRandom Baseline ({n_episodes} episodes):")
    print(f"  Capture rate:      {summary['capture_rate']:.1%}")
    print(f"  Coop capture rate: {summary['coop_capture_rate']:.1%}")
    print(f"  Mean return:       {summary['mean_return']:.2f}")
    print(f"  Mean length:       {summary['mean_length']:.1f}")

    os.makedirs("results", exist_ok=True)
    metrics.plot("results/random_training.png", title="Random Agent Baseline")
    print("  Plot saved to results/random_training.png")


if __name__ == "__main__":
    main()
