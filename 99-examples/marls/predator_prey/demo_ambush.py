"""Demo: block-and-hunt ambush in a walled room (env1).

Shows a scripted sequence where P0 (blocker) seals the room's only exit
while P1 (hunter) sweeps the prey toward the blocker. This illustrates
the cooperative strategy that MARL agents can learn.

Usage:
    python demo_ambush.py              # ASCII output (env1)
    python demo_ambush.py --render     # pygame visualization
    python demo_ambush.py --env env0   # original open grid
    python demo_ambush.py --env env1   # room with single exit (default)
"""

import argparse
import time

from predator_prey.env import PredatorPreyEnv, MAPS

try:
    from predator_prey.env.renderer import Renderer
    HAS_RENDERER = True
except ImportError:
    HAS_RENDERER = False


def print_grid(walls, preds, prey, grid_size, step, commentary=""):
    """Print ASCII grid with walls, predators, and prey."""
    print(f"\n--- Step {step} ---")
    if commentary:
        print(f"  {commentary}")
    print(f"  P0(blocker)={preds[0]}  P1(hunter)={preds[1]}  Prey={prey}")
    print()

    for r in range(grid_size):
        row_str = ""
        for c in range(grid_size):
            cell = (r, c)
            if cell in walls:
                row_str += "  #  "
            else:
                contents = []
                if cell == preds[0]:
                    contents.append("B")
                if cell == preds[1]:
                    contents.append("H")
                if cell == prey:
                    contents.append("Y")
                if contents:
                    label = "".join(contents)
                    row_str += f" [{label:^3}]"
                else:
                    row_str += "  .  "
        print(f"  {r} {row_str}")
    print(f"    {''.join(f'  {c}  ' for c in range(grid_size))}")


# Scripted frames for env1: room with exit at (5,3)
# Each frame: (blocker_pos, hunter_pos, prey_pos, commentary)
ENV1_FRAMES = [
    ((6, 3), (2, 3), (3, 3),
     "Initial: Hunter above prey, blocker approaching exit from south."),
    ((5, 3), (2, 3), (4, 3),
     "Blocker seals exit! Prey flees south from hunter but exit is blocked."),
    ((5, 3), (3, 3), (4, 4),
     "Prey dodges right. Hunter advances into room center."),
    ((5, 3), (3, 4), (4, 3),
     "Hunter flanks right, cutting off that escape. Prey forced back center."),
    ((5, 3), (4, 4), (3, 3),
     "Hunter moves down-right. Prey retreats north to (3,3)."),
    ((5, 3), (3, 4), (2, 3),
     "Hunter pressures from east. Prey pushed to top of room."),
    ((5, 3), (2, 4), (2, 2),
     "Hunter flanks to (2,4). Prey cornered at (2,2) against walls."),
    ((5, 3), (3, 2), (2, 3),
     "Hunter sweeps to (3,2), blocking south-left. Prey dodges to (2,3)."),
    ((5, 3), (2, 2), (3, 3),
     "Hunter mirrors to (2,2). Prey drops to center."),
    ((5, 3), (3, 3), (4, 3),
     "Hunter on center! Prey forced south toward the blocked exit."),
    ((5, 3), (4, 3), (4, 2),
     "Hunter follows. Prey dodges left -- but it's a dead end."),
    ((5, 3), (4, 2), (4, 2),
     ">>> CAPTURE! Hunter lands on prey at (4,2). Blocker held exit. <<<"),
]

# Scripted frames for env0: open grid corner trap
ENV0_FRAMES = [
    ((4, 5), (2, 1), (2, 4),
     "Initial: Hunter at (2,1), prey at (2,4), blocker at (4,5)."),
    ((3, 5), (2, 2), (1, 5),
     "Hunter advances right. Prey flees toward top-right. Blocker moves up."),
    ((2, 5), (1, 3), (0, 6),
     "Blocker reaches row 2! Hunter on row 1. Prey cornered at (0,6)."),
    ((1, 6), (0, 5), (0, 6),
     "Blocker seals (1,6). Hunter at (0,5). Prey trapped in corner!"),
    ((1, 6), (0, 6), (0, 6),
     ">>> CAPTURE! Hunter lands on prey. Blocker blocked escape. <<<"),
]


def run_demo(env_name="env1", use_renderer=False):
    map_cfg = MAPS[env_name]
    walls = map_cfg["walls"]
    grid_size = 7

    frames = ENV1_FRAMES if env_name == "env1" else ENV0_FRAMES

    print("=" * 64)
    print(f"  AMBUSH DEMO on {env_name}: {map_cfg['description']}")
    print("=" * 64)
    print()
    print("  P0 (B) = BLOCKER  -- seals the escape route")
    print("  P1 (H) = HUNTER   -- sweeps prey toward the blocker")
    print("  Y      = PREY")
    print()
    if env_name == "env1":
        print("  The room (rows 2-4, cols 2-4) has ONE exit at (5,3).")
        print("  The blocker guards the exit while the hunter sweeps inside.")
    else:
        print("  On the open grid, the blocker cuts off the prey's escape")
        print("  path while the hunter drives it into a corner.")

    renderer = None
    if use_renderer and HAS_RENDERER:
        renderer = Renderer(grid_size)

    for i, (b_pos, h_pos, y_pos, commentary) in enumerate(frames):
        print_grid(walls, [b_pos, h_pos], y_pos, grid_size, i, commentary)

        if renderer:
            frame_data = {
                "predators": [b_pos, h_pos],
                "prey": y_pos,
                "step": i,
                "walls": walls,
            }
            if not renderer.render_frame(frame_data, fps=1,
                                         episode=1, total_episodes=1):
                break

    if renderer:
        time.sleep(3)
        renderer.close()


def main():
    parser = argparse.ArgumentParser(description="Block-and-hunt ambush demo")
    parser.add_argument("--env", choices=list(MAPS.keys()), default="env1",
                        help="Map to use (default: env1)")
    parser.add_argument("--render", action="store_true",
                        help="Use pygame renderer")
    args = parser.parse_args()

    run_demo(env_name=args.env, use_renderer=args.render)


if __name__ == "__main__":
    main()
