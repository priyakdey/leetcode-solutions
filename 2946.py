"""
2946. Matrix Similarity After Cyclic Shifts

You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.

The following proccess happens k times:

- Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
- Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.

Return true if the final modified matrix after k steps is identical to the
original matrix, and false otherwise.
"""

import copy
from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        copy_mat = copy.deepcopy(mat)

        rows, cols = len(mat), len(mat[0])
        k = k % cols

        if k == 0:
            return True

        for i, row in enumerate(copy_mat):
            if i & 1 == 0:
                self.rotate_left(row, k)
            else:
                self.rotate_right(row, k)

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] != copy_mat[row][col]:
                    return False

        return True

    def rotate_right(self, arr: List[int], k: int) -> None:
        self.reverse(arr, 0, len(arr) - 1)
        self.reverse(arr, 0, k - 1)
        self.reverse(arr, k, len(arr) - 1)

    def rotate_left(self, arr: List[int], k: int) -> None:
        self.reverse(arr, 0, len(arr) - 1)
        self.reverse(arr, 0, len(arr) - 1 - k)
        self.reverse(arr, len(arr) - k, len(arr) - 1)

    @staticmethod
    def reverse(arr: List[int], start: int, end: int) -> None:
        """Reverses an array from start to end, both inclusive"""
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
