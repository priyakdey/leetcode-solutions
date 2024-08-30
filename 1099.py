"""
1099. Two Sum Less Than K

Given an array nums of integers and integer k, return the maximum sum such that
there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist
satisfying this equation, return -1.
"""

from typing import List


INT_MAX = (1 << 31) - 1


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if k > nums[i] + nums[j] > max_sum:
                    max_sum = nums[i] + nums[j]

        return max_sum
