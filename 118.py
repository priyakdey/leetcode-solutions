"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        levels = [[1], [1, 1]]

        for i in range(3, numRows + 1):
            level = [1]
            for i in range(1, len(levels[-1])):
                level.append(levels[-1][i] + levels[-1][i - 1])
            level.append(1)
            levels.append(level)

        return levels
