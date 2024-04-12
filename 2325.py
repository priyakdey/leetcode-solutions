"""
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in 
the same order (i.e., an equal array).
"""

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        row_repr_map = {}

        for row in grid:
            key = str(row)
            if key not in row_repr_map:
                row_repr_map[key] = 1
            else:
                row_repr_map[key] += 1

        pairs = 0

        buffer = []

        for col in range(cols):
            for row in range(rows):
                buffer.append(grid[row][col])
            key = str(buffer)
            if key in row_repr_map:
                pairs += row_repr_map[key]
            buffer.clear()

        return pairs
