"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value target in an m x n 
integer matrix matrix. This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        row, col = rows - 1, 0
        is_target_found = False

        while row >= 0 and col < cols:
            if matrix[row][col] == target:
                is_target_found = True
                break
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1

        return is_target_found
