"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of 
the squares of each number sorted in non-decreasing order.
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares: List[int] = [0 for _ in nums]
        length = len(squares)
        cursor = length - 1
        left, right = 0, length - 1

        while left <= right:
            a, b = nums[left] ** 2, nums[right] ** 2
            if a >= b:
                squares[cursor] = a
                left += 1
            else:
                squares[cursor] = b
                right -= 1
            cursor -= 1

        return squares
