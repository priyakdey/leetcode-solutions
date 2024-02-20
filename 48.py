"""
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 
90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # transpose the matrix
        for row in range(n):
            for col in range(row, n):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1
