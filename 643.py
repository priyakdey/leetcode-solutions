"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum 
average value and return this value. Any answer with a calculation error less 
than 10-5 will be accepted.
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total_sum = 0
        for i in range(k):
            total_sum += nums[i]

        max_avg = total_sum / k

        for i in range(k, len(nums)):
            total_sum = total_sum + nums[i] - nums[i - k]
            avg = total_sum / k
            max_avg = max(max_avg, avg)

        return max_avg
