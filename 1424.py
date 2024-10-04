"""
1424. Diagonal Traverse II

Given a 2D integer array nums, return all elements of nums in diagonal order as
shown in the below images.
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows, cols = len(nums), 0
        element_count = 0
        for row in nums:
            length = len(row)
            element_count += length
            cols = max(cols, length)

        arr: List[int] = [0] * element_count
        curr = 0

        for r in range(rows):
            row, col = r, 0
            while 0 <= row < rows and 0 <= col < cols:
                if col < len(nums[row]):
                    arr[curr] = nums[row][col]
                    curr += 1
                row -= 1
                col += 1

        for c in range(1, cols):
            row, col = rows -1, c
            while 0 <= row < rows and 0 <= col < cols:
                if col < len(nums[row]):
                    arr[curr] = nums[row][col]
                    curr += 1
                row -= 1
                col += 1

        return arr



