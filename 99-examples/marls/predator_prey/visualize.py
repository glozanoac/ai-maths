"""Visualize trained agents playing with pygame."""

import argparse
import numpy as np

from predator_prey.env import PredatorPreyEnv, MAPS
from predator_prey.env.renderer import Renderer
from predator_prey.agents import RandomAgent, IQLAgent, VDNAgent


def run_episode(env, select_action_fn):
    """Run one episode and collect position frames."""
    obs = env.reset()
    frames = [env.get_positions()]
    done = False

    while not done:
        actions = select_action_fn(obs)
        obs, rewards, dones, infos = env.step(actions)
        frames.append(env.get_positions())
        done = dones["__all__"]

    return frames, infos


def main():
    parser = argparse.ArgumentParser(description="Visualize agents")
    parser.add_argument("--agent", choices=["random", "iql", "vdn"], default="random")
    parser.add_argument("--env", choices=list(MAPS.keys()), default="env0")
    parser.add_argument("--episodes", type=int, default=5)
    parser.add_argument("--fps", type=int, default=5)
    args = parser.parse_args()

    reward_mode = "cooperative" if args.agent == "vdn" else "individual"
    env = PredatorPreyEnv(reward_mode=reward_mode, walls=MAPS[args.env]["walls"])

    if args.agent == "random":
        agents = {name: RandomAgent() for name in env.agents}
        select_fn = lambda obs: {name: agents[name].select_action(obs[name], explore=False) for name in env.agents}
    elif args.agent == "iql":
        agents = {}
        for name in env.agents:
            agent = IQLAgent()
            agent.load(f"checkpoints/iql_{name}.pkl")
            agents[name] = agent
        select_fn = lambda obs: {name: agents[name].select_action(obs[name], explore=False) for name in env.agents}
    elif args.agent == "vdn":
        vdn = VDNAgent()
        vdn.load("checkpoints/vdn.pt")
        select_fn = lambda obs: {name: vdn.select_action(obs[name], agent_idx=i, explore=False) for i, name in enumerate(env.agents)}

    renderer = Renderer(env.grid_size)

    for ep in range(args.episodes):
        frames, infos = run_episode(env, select_fn)
        captured = "CAPTURED" if infos["captured"] else "ESCAPED"
        print(f"Episode {ep+1}: {captured} in {infos['step']} steps")
        renderer.render_episode(frames, fps=args.fps, episode=ep + 1, total_episodes=args.episodes)

    renderer.close()


if __name__ == "__main__":
    main()
