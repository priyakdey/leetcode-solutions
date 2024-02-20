"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire 
row and column to 0's.

You must do it in place.
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def fillRowWithZero(row: int) -> None:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0

        def fillColWithZero(col: int) -> None:
            for i in range(len(matrix)):
                matrix[i][col] = 0

        is_first_row_zero, is_first_col_zero = False, False

        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                is_first_row_zero = True
                break

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                is_first_col_zero = True
                break

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                fillRowWithZero(row)

        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                fillColWithZero(col)

        if is_first_row_zero:
            fillRowWithZero(0)
        if is_first_col_zero:
            fillColWithZero(0)
