"""
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents 
land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is 
completely surrounded by water, and there is exactly one island (i.e., one or 
more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the 
water around the island. One cell is a square with side length 1. The grid is 
rectangular, width and height don't exceed 100. Determine the perimeter of 
the island.
"""

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    if row - 1 >= 0 and grid[row - 1][col] == 0:
                        perimeter += 1
                    if row + 1 < rows and grid[row + 1][col] == 0:
                        perimeter += 1
                    if col - 1 >= 0 and grid[row][col - 1] == 0:
                        perimeter += 1
                    if col + 1 < cols and grid[row][col + 1] == 0:
                        perimeter += 1
                    if row - 1 == -1:
                        perimeter += 1
                    if row + 1 == rows:
                        perimeter += 1
                    if col - 1 == -1:
                        perimeter += 1
                    if col + 1 == cols:
                        perimeter += 1

        return perimeter
