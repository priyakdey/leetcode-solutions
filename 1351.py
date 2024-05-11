"""
1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise 
and column-wise, return the number of negative numbers in grid.
"""

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or grid[0] is None or len(grid[0]) == 0:
            raise Exception("Invalid input")

        rows, cols = len(grid), len(grid[0])

        row, col = rows - 1, 0
        count = 0

        while row >= 0 and col < cols:
            if grid[row][col] < 0:
                count += cols - 1 - col + 1
                row = row - 1
            else:
                col = col + 1

        return count
