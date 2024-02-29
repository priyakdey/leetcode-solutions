"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are all 
surrounded by water.
"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        island_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_count += 1
                    queue: Deque[Tuple[int, int]] = deque()
                    queue.append((row, col))
                    grid[row][col] = "-1"

                    while len(queue) != 0:
                        r, c = queue.popleft()

                        if r - 1 >= 0 and grid[r - 1][c] == "1":
                            grid[r - 1][c] = "-1"
                            queue.append((r - 1, c))
                        if r + 1 < rows and grid[r + 1][c] == "1":
                            grid[r + 1][c] = "-1"
                            queue.append((r + 1, c))
                        if c - 1 >= 0 and grid[r][c - 1] == "1":
                            grid[r][c - 1] = "-1"
                            queue.append((r, c - 1))
                        if c + 1 < cols and grid[r][c + 1] == "1":
                            grid[r][c + 1] = "-1"
                            queue.append((r, c + 1))

        return island_count
