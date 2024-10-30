"""
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

from collections import deque
from typing import Deque, List, Set, Tuple


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue: Deque[Tuple[int, int]] = deque()
        visited: Set[Tuple[int, int]] = set()
        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        max_area: int = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 or (row, col) in visited:
                    continue

                queue.append((row, col))
                visited.add((row, col))
                count = 1

                while len(queue) > 0:
                    r, c = queue.popleft()

                    for dr, dc in directions:
                        next_row, next_col = r + dr, c + dc
                        if (
                            0 <= next_row < rows
                            and 0 <= next_col < cols
                            and grid[next_row][next_col] == 1
                            and (next_row, next_col) not in visited
                        ):
                            queue.append((next_row, next_col))
                            visited.add((next_row, next_col))
                            count += 1

                total_area = count * 1
                max_area = max(max_area, total_area)

        return max_area
