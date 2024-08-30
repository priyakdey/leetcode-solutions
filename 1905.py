"""
1905. Count Sub Islands

You are given two m x n binary matrices grid1 and grid2 containing only 0's
(representing water) and 1's (representing land). An island is a group of 1's
connected 4-directionally (horizontal or vertical). Any cells outside of the
grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1
that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.
"""

from collections import deque
from typing import Deque, List, Set, Tuple


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        queue: Deque[Tuple[int, int]] = deque()
        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        island_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid1[row][col] == grid2[row][col] == 1:
                    island_count += 1
                    queue.append((row, col))
                    grid1[row][col] = -1

                    while len(queue) > 0:
                        row, col = queue.popleft()

                        for dy, dx in directions:
                            next_row = row + dy
                            next_col = col + dx
                            if (
                                0 <= next_row < rows
                                and 0 <= next_col < cols
                                and grid1[next_row][next_col] == 1
                                and grid2[next_row][next_col] == 1
                            ):
                                queue.append((next_row, next_col))
                                grid1[next_row][next_col] = -1

        for row in grid1:
            print(row)

        for row in grid2:
            print(row)

        return island_count
