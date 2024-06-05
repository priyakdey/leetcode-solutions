"""
304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its 
upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

- NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
- int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the 
  elements of matrix inside the rectangle defined by its upper left corner 
  (row1, col1) and lower right corner (row2, col2).

You must design an algorithm where sumRegion works on O(1) time complexity.
"""

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.cache = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for row in range(rows):
            for col in range(cols):
                self.cache[row + 1][col + 1] = (
                    self.cache[row + 1][col]
                    + self.cache[row][col + 1]
                    + matrix[row][col]
                    - self.cache[row][col]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.cache[row2 + 1][col2 + 1]
            + self.cache[row1][col1]
            - self.cache[row1][col2 + 1]
            - self.cache[row2 + 1][col1]
        )
