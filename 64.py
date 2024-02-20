"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left 
to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        min_path_sum = list(grid[-1])

        for col in range(cols - 2, -1, -1):
            min_path_sum[col] = min_path_sum[col] + min_path_sum[col + 1]

        for row in range(rows - 2, -1, -1):
            min_path_sum[-1] = min_path_sum[-1] + grid[row][-1]

            for col in range(cols - 2, -1, -1):
                min_path_sum[col] = min(
                    grid[row][col] + min_path_sum[col],
                    grid[row][col] + min_path_sum[col + 1],
                )

        return min_path_sum[0]
