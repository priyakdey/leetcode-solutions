"""
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the 
left of the index is equal to the sum of all the numbers strictly to the index's 
right.

If the index is on the left edge of the array, then the left sum is 0 because 
there are no elements to the left. This also applies to the right edge of the 
array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        left_sum, right_sum = 0, total_sum
        index = -1

        for i, num in enumerate(nums):
            right_sum -= num

            if left_sum == right_sum:
                index = i
                break

            left_sum += num

        return index
