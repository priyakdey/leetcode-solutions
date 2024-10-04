"""
874. Walking Robot Simulation

A robot on an infinite XY-plane starts at point (0, 0) facing north.
The robot can receive a sequence of these three possible types of commands:

- -2: Turn left 90 degrees.
- -1: Turn right 90 degrees.
- 1 <= k <= 9: Move forward k units, one unit at a time.

Some of the grid squares are obstacles. The ith obstacle is at grid point
obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will
instead stay in its current location and move on to the next command.

Return the maximum Euclidean distance that the robot ever gets from the
origin squared (i.e. if the distance is 5, return 25).

Note:
- North means +Y direction.
- East means +X direction.
- South means -Y direction.
- West means -X direction.
- There can be obstacle in [0,0].
"""

from typing import Dict, List, Set, Tuple


type Direction = Tuple[int, int]

NORTH: Direction = (0, 1)
SOUTH: Direction = (0, -1)
EAST: Direction = (1, 0)
WEST: Direction = (-1, 0)


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        walls: Set[Direction] = {(x, y) for x, y in obstacles}
        direction_table: Dict[int, Dict[Direction, Direction]] = {
            -1: {NORTH: EAST, SOUTH: WEST, EAST: SOUTH, WEST: NORTH},
            -2: {
                NORTH: WEST,
                SOUTH: EAST,
                EAST: NORTH,
                WEST: SOUTH,
            },
        }

        x, y = 0, 0
        curr_direction: Direction = NORTH
        furthest: int = 0

        for command in commands:
            match command:
                case -1 | -2:
                    curr_direction = direction_table[command][curr_direction]
                case _:
                    for i in range(command):
                        next_x, next_y = x + curr_direction[0], y + curr_direction[1]
                        if (next_x, next_y) in walls:
                            break
                        x, y = next_x, next_y
                    furthest = max(furthest, (x * x) + (y * y))

        return furthest
