"""
325. Maximum Size Subarray Sum Equals k

Given an integer array nums and an integer k, return the maximum length of a
subarray that sums to k. If there is not one, return 0 instead.
"""

from typing import List, Dict


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum_map: Dict[int, int] = {}
        prefix_sum = 0
        max_length = 0

        for index, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = index

            if prefix_sum == k:
                max_length = max(max_length, index - 0 + 1)

            compliment = k - prefix_sum
            if compliment in prefix_sum_map:
                length = index - (prefix_sum_map[compliment] + 1) + 1
                max_length = max(max_length, length)

        return max_length
