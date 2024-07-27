"""
498. Diagonal Traverse

Given an m x n matrix mat, return an array of all the elements of the array in a
diagonal order.
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if mat is None or len(mat) == 0 or mat[0] is None or len(mat[0]) == 0:
            raise Exception("invalid arguments")

        rows, cols = len(mat), len(mat[0])

        row, col = 0, 0
        going_up = True
        elements: List[int] = [0] * rows * cols
        curr = 0

        for _ in range(rows * cols):
            elements[curr] = mat[row][col]
            curr += 1

            if going_up:
                if col + 1 == cols:
                    row, col = row + 1, cols - 1
                    going_up = False
                elif row - 1 == -1:
                    row, col = 0, col + 1
                    going_up = False
                else:
                    row, col = row - 1, col + 1
            else:
                if row + 1 == rows:
                    row, col = rows - 1, col + 1
                    going_up = True
                elif col - 1 == -1:
                    row, col = row + 1, 0
                    going_up = True
                else:
                    row, col = row + 1, col - 1

        return elements
