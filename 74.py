"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowCount, colCount = len(matrix), len(matrix[0])

        # check the row
        up, down = 0, rowCount - 1
        row = -1
        while up <= down:
            mid = up + (down - up) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break

            if target < matrix[mid][0]:
                down = mid - 1
            else:
                up = mid + 1

        if row == -1:
            return False

        left, right = 0, colCount - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == matrix[row][mid]:
                return True

            if target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False
