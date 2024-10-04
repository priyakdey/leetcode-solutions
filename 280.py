"""
280. Wiggle Sort

Given an integer array nums, reorder it such that
nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.
"""
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        curr = 0

        while left <= right:
            nums[curr] = sorted_nums[left]
            left += 1
            curr += 1
            if curr != len(nums):
                nums[curr] = sorted_nums[right]
            right -= 1
            curr += 1
