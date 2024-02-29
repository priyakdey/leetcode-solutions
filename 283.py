"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr, insert_at = 0, 0
        length = len(nums)

        while curr < length:
            if nums[curr] != 0:
                nums[insert_at] = nums[curr]
                insert_at += 1
            curr += 1

        for i in range(insert_at, len(nums)):
            nums[i] = 0
