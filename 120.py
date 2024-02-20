"""
120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move to either 
index i or index i + 1 on the next row.
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        INT_MAX = (1 << 31) - 1

        rows, cols = len(triangle), len(triangle[-1])
        max_sum: List[List[int]] = [[INT_MAX for _ in range(cols)] for _ in range(rows)]

        for i, num in enumerate(triangle[0]):
            max_sum[0][i] = num

        for i in range(1, len(triangle)):
            row = triangle[i]
            for j, num in enumerate(row):
                if j - 1 >= 0:
                    max_sum[i][j] = max_sum[i - 1][j - 1] + triangle[i][j]
                if j < len(row):
                    max_sum[i][j] = min(
                        max_sum[i][j], max_sum[i - 1][j] + triangle[i][j]
                    )

        return min(max_sum[-1])
