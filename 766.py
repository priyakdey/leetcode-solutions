"""
766. Toeplitz Matrix

Given an m x n matrix, return true if the matrix is Toeplitz.
Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the
same elements.
"""

from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        value = matrix[0][0]
        row, col = 1, 1
        while row < rows and col < cols and matrix[row][col] == value:
            row += 1
            col += 1

        if row != rows and col != cols:
            return False

        for row in range(1, rows):
            col = 0
            value = matrix[row][col]
            while row < rows and col < cols and matrix[row][col] == value:
                row += 1
                col += 1
            if row != rows:
                return False

        for col in range(1, cols):
            row = 0
            value = matrix[row][col]
            while row < rows and col < cols and matrix[row][col] == value:
                row += 1
                col += 1
            if col != cols:
                return False

        return True
