"""
918. Maximum Sum Circular Subarray
Medium
Topics
Companies
Hint
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
"""

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_overall, max_till = nums[0], nums[0]
        min_overall, min_till = nums[0], nums[0]
        total_sum = nums[0]

        for i in range(1, len(nums)):
            max_till = max(max_till + nums[i], nums[i])
            max_overall = max(max_overall, max_till)

            min_till = min(min_till + nums[i], nums[i])
            min_overall = min(min_overall, min_till)

            total_sum += nums[i]

        if total_sum == min_overall:
            return max_overall

        return max(max_overall, total_sum - min_overall)
