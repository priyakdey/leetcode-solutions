"""
1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear
path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected
(i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.
"""

from typing import List, Set, Tuple


INT_MAX = (1 << 31) - 1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        paths: List[List[int]] = [[INT_MAX for _ in range(cols)] for _ in range(rows)]
        paths[0][0] = 1
        visited: Set[Tuple[int, int]] = set()

        for row in range(rows):
            for col in range(cols):
                visited.add((row, col))

                if grid[row][col] == 1:
                    continue

                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dc == 0 and dr == 0:
                            continue

                        next_row, next_col = row + dr, col + dc
                        if (
                            0 <= next_row < rows
                            and 0 <= next_col < cols
                            and grid[next_row][next_col] != 1
                            and (next_row, next_col) not in visited
                        ):
                            paths[next_row][next_col] = min(
                                paths[next_row][next_col], 1 + paths[row][col]
                            )

        return paths[-1][-1] if paths[-1][-1] != INT_MAX else -1
