"""Train Independent Q-Learning agents."""

import os

from tqdm import trange

from predator_prey.env import PredatorPreyEnv
from predator_prey.agents import IQLAgent
from predator_prey.utils import MetricsTracker


def main():
    env = PredatorPreyEnv(reward_mode="individual")
    agents = {name: IQLAgent() for name in env.agents}
    metrics = MetricsTracker()
    n_episodes = 10000

    for ep in trange(n_episodes, desc="IQL"):
        obs = env.reset()
        episode_return = 0
        done = False

        while not done:
            actions = {name: agents[name].select_action(obs[name]) for name in env.agents}
            next_obs, rewards, dones, infos = env.step(actions)

            for name in env.agents:
                agents[name].learn(obs[name], actions[name], rewards[name],
                                   next_obs[name], dones[name])

            episode_return += sum(rewards.values()) / len(env.agents)
            obs = next_obs
            done = dones["__all__"]

        metrics.record(episode_return, infos["step"], infos["captured"], infos["cooperative_capture"])

        if (ep + 1) % 2000 == 0:
            s = metrics.summary(last_n=500)
            eps = agents[env.agents[0]].epsilon
            print(f"\n  [Ep {ep+1}] capture={s['capture_rate']:.1%}, "
                  f"return={s['mean_return']:.2f}, eps={eps:.3f}")

    # Save
    os.makedirs("checkpoints", exist_ok=True)
    for name, agent in agents.items():
        agent.save(f"checkpoints/iql_{name}.pkl")

    os.makedirs("results", exist_ok=True)
    metrics.plot("results/iql_training.png", title="IQL Training")

    summary = metrics.summary()
    print(f"\nIQL Final ({n_episodes} episodes):")
    print(f"  Capture rate:      {summary['capture_rate']:.1%}")
    print(f"  Coop capture rate: {summary['coop_capture_rate']:.1%}")
    print(f"  Mean return:       {summary['mean_return']:.2f}")
    print(f"  Mean length:       {summary['mean_length']:.1f}")
    print(f"  Q-table sizes:     {[len(a.q_table) for a in agents.values()]}")
    print("  Plot saved to results/iql_training.png")


if __name__ == "__main__":
    main()
