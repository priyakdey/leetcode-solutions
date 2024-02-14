"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return 
its sum.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None:
            raise Exception("invalid input")

        max_overall = nums[0]
        max_till = nums[0]
        for i in range(1, len(nums)):
            max_till = max(max_till + nums[i], nums[i])
            max_overall = max(max_overall, max_till)

        return max_overall
