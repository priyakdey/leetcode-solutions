"""
1590. Make Sum Divisible by P

Given an array of positive integers nums, remove the smallest subarray
(possibly empty) such that the sum of the remaining elements is divisible by p.
It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1
if it's impossible.

A subarray is defined as a contiguous block of elements in the array.
"""

from typing import Dict, List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remove = total_sum % p
        if remove == 0:
            return 0

        lookup: Dict[int, int] = {}
        cumm_sum: int = 0
        length = len(nums)

        for i, num in enumerate(nums):
            cumm_sum += num
            if cumm_sum == remove:
                length = min(length, i - 0 + 1)
            compliment = cumm_sum - remove
            if compliment in lookup:
                length = min(length, i - lookup[compliment])
            lookup[cumm_sum] = i

        return length if length != len(nums) else -1
