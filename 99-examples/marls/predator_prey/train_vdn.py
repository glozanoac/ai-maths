"""Train VDN (Value Decomposition Network) agents."""

import argparse
import os

import numpy as np
from tqdm import trange

from predator_prey.env import PredatorPreyEnv, MAPS
from predator_prey.agents import VDNAgent
from predator_prey.utils import ReplayBuffer, MetricsTracker


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", choices=list(MAPS.keys()), default="env0")
    args = parser.parse_args()

    env = PredatorPreyEnv(reward_mode="cooperative", walls=MAPS[args.env]["walls"])
    vdn = VDNAgent()
    buffer = ReplayBuffer(capacity=50000)
    metrics = MetricsTracker()
    n_episodes = 5000
    warmup = 1000  # steps before learning starts
    total_steps = 0

    for ep in trange(n_episodes, desc="VDN"):
        obs = env.reset()
        episode_return = 0
        done = False

        while not done:
            # Select actions
            actions = {}
            for i, name in enumerate(env.agents):
                actions[name] = vdn.select_action(obs[name], agent_idx=i)

            next_obs, rewards, dones, infos = env.step(actions)

            # Store joint transition
            obs_array = np.array([obs[name] for name in env.agents])
            next_obs_array = np.array([next_obs[name] for name in env.agents])
            action_array = np.array([actions[name] for name in env.agents])
            team_reward = sum(rewards.values()) / len(env.agents)

            buffer.push(obs_array, action_array, team_reward, next_obs_array, dones["__all__"])

            # Learn
            total_steps += 1
            if total_steps > warmup:
                vdn.learn(buffer)

            episode_return += team_reward
            obs = next_obs
            done = dones["__all__"]

        metrics.record(episode_return, infos["step"], infos["captured"], infos["cooperative_capture"])

        if (ep + 1) % 1000 == 0:
            s = metrics.summary(last_n=500)
            print(f"\n  [Ep {ep+1}] capture={s['capture_rate']:.1%}, "
                  f"coop={s['coop_capture_rate']:.1%}, "
                  f"return={s['mean_return']:.2f}, eps={vdn.epsilon:.3f}")

    # Save
    os.makedirs("checkpoints", exist_ok=True)
    vdn.save("checkpoints/vdn.pt")

    os.makedirs("results", exist_ok=True)
    metrics.plot("results/vdn_training.png", title="VDN Training")

    summary = metrics.summary()
    print(f"\nVDN Final ({n_episodes} episodes):")
    print(f"  Capture rate:      {summary['capture_rate']:.1%}")
    print(f"  Coop capture rate: {summary['coop_capture_rate']:.1%}")
    print(f"  Mean return:       {summary['mean_return']:.2f}")
    print(f"  Mean length:       {summary['mean_length']:.1f}")
    print("  Plot saved to results/vdn_training.png")


if __name__ == "__main__":
    main()
