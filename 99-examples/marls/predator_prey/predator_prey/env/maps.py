"""Map configurations for PredatorPreyEnv."""


def _parse_grid(lines):
    """Parse ASCII grid into a set of wall coordinates.
    '#' = wall, '.' = open space.
    """
    walls = set()
    for r, line in enumerate(lines):
        for c, ch in enumerate(line.split()):
            if ch == "#":
                walls.add((r, c))
    return walls


# env0: Original open 7x7 grid (no walls)
ENV0_WALLS = set()

# env1: Enclosed room with a single exit at (5, 3).
#
#   . . . . . . .    row 0
#   . # # # # # .    row 1
#   . # . . . # .    row 2   <- room interior (3x3)
#   . # . . . # .    row 3
#   . # . . . # .    row 4
#   . # # . # # .    row 5   <- exit at column 3
#   . . . . . . .    row 6
#
# The prey starts inside the room. P0 (blocker) guards the exit
# from outside. P1 (hunter) starts inside and pushes the prey
# toward the exit. The prey gets squeezed between the hunter
# (above) and the blocker (at the exit).
ENV1_WALLS = _parse_grid([
    ". . . . . . .",
    ". # # # # # .",
    ". # . . . # .",
    ". # . . . # .",
    ". # . . . # .",
    ". # # . # # .",
    ". . . . . . .",
])

# Spawn positions for the ambush scenario:
# - Hunter directly above prey (same column) to push straight down
# - Blocker outside the exit, will move to seal it
ENV1_SPAWNS = {
    "predator_0": (6, 3),   # blocker: outside the exit
    "predator_1": (2, 3),   # hunter: top of room, above prey
    "prey": (3, 3),         # prey: room center
}


MAPS = {
    "env0": {"walls": ENV0_WALLS, "description": "Open 7x7 grid (default)"},
    "env1": {"walls": ENV1_WALLS, "spawns": ENV1_SPAWNS,
             "description": "Room with single exit (block-and-hunt)"},
}
