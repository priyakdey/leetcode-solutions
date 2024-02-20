"""
63. Unique Paths II

You are given an m x n integer array grid. There is a robot initially located 
at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. 
A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach 
the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 
2 * 109.
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        ways = [[0 for _ in range(cols)] for _ in range(rows)]

        ways[-1][-1] = 1

        for col in range(cols - 2, -1, -1):
            if obstacleGrid[-1][col] == 1:
                ways[-1][col] = 0
            else:
                ways[-1][col] = ways[-1][col + 1]

        for row in range(rows - 2, -1, -1):
            if obstacleGrid[row][-1] == 1:
                ways[row][-1] = 0
            else:
                ways[row][-1] = ways[row + 1][-1]

        for row in range(rows - 2, -1, -1):
            for col in range(cols - 2, -1, -1):
                if obstacleGrid[row][col] == 1:
                    ways[row][col] = 0
                else:
                    ways[row][col] = ways[row + 1][col] + ways[row][col + 1]

        return ways[0][0]
