"""Compare trained policies: Random vs IQL vs VDN."""

import argparse
import os

import numpy as np
from tqdm import trange

from predator_prey.env import PredatorPreyEnv, MAPS
from predator_prey.agents import RandomAgent, IQLAgent, VDNAgent
from predator_prey.utils import MetricsTracker


def evaluate(env, select_action_fn, n_episodes=100, desc="Eval"):
    metrics = MetricsTracker()
    for _ in trange(n_episodes, desc=desc, leave=False):
        obs = env.reset()
        episode_return = 0
        done = False

        while not done:
            actions = select_action_fn(obs)
            next_obs, rewards, dones, infos = env.step(actions)
            episode_return += sum(rewards.values()) / len(env.agents)
            obs = next_obs
            done = dones["__all__"]

        metrics.record(episode_return, infos["step"], infos["captured"], infos["cooperative_capture"])

    return metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", choices=list(MAPS.keys()), default="env0")
    args = parser.parse_args()

    walls = MAPS[args.env]["walls"]
    n_eval = 200
    results = {}

    # Random baseline
    env = PredatorPreyEnv(walls=walls)
    random_agents = {name: RandomAgent() for name in env.agents}
    random_metrics = evaluate(
        env,
        lambda obs: {name: random_agents[name].select_action(obs[name], explore=False) for name in env.agents},
        n_eval, "Random"
    )
    results["Random"] = random_metrics

    # IQL
    iql_agents = {}
    for name in env.agents:
        agent = IQLAgent()
        path = f"checkpoints/iql_{name}.pkl"
        if os.path.exists(path):
            agent.load(path)
            iql_agents[name] = agent
        else:
            print(f"Warning: {path} not found, skipping IQL evaluation")
            iql_agents = None
            break

    if iql_agents:
        iql_metrics = evaluate(
            env,
            lambda obs: {name: iql_agents[name].select_action(obs[name], explore=False) for name in env.agents},
            n_eval, "IQL"
        )
        results["IQL"] = iql_metrics

    # VDN
    vdn_path = "checkpoints/vdn.pt"
    if os.path.exists(vdn_path):
        env_coop = PredatorPreyEnv(reward_mode="cooperative", walls=walls)
        vdn = VDNAgent()
        vdn.load(vdn_path)
        vdn_metrics = evaluate(
            env_coop,
            lambda obs: {name: vdn.select_action(obs[name], agent_idx=i, explore=False) for i, name in enumerate(env.agents)},
            n_eval, "VDN"
        )
        results["VDN"] = vdn_metrics
    else:
        print(f"Warning: {vdn_path} not found, skipping VDN evaluation")

    # Print comparison table
    print("\n" + "=" * 65)
    print(f"{'Method':<10} {'Capture%':>10} {'Coop%':>10} {'Return':>10} {'Length':>10}")
    print("-" * 65)
    for name, m in results.items():
        s = m.summary(last_n=n_eval)
        print(f"{name:<10} {s['capture_rate']:>9.1%} {s['coop_capture_rate']:>9.1%} "
              f"{s['mean_return']:>10.2f} {s['mean_length']:>10.1f}")
    print("=" * 65)

    # Comparison plot
    os.makedirs("results", exist_ok=True)
    if len(results) > 1:
        trackers = list(results.values())
        labels = list(results.keys())
        MetricsTracker.compare_plot(trackers, labels, "results/comparison.png", window=20)
        print("\nComparison plot saved to results/comparison.png")


if __name__ == "__main__":
    main()
