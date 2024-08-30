"""
3247. Number of Subsequences with Odd Sum

Given an array nums, return the number of subsequences with an odd sum of
elements.

Since the answer may be very large, return it modulo 10^9 + 7.
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def subsequenceCount(self, nums: List[int]) -> int:
        def generate(index: int, curr_sum: int, cache: List[List[int]]) -> int:
            if index == len(nums):
                return 1 if curr_sum & 1 == 1 else 0

            if cache[index][curr_sum] != -1:
                return cache[index][curr_sum]

            count = (
                generate(index + 1, curr_sum, cache)
                + generate(index + 1, curr_sum + nums[index], cache)
            ) % MOD

            cache[index][curr_sum] = count
            return count

        max_sum = sum(nums)
        length = len(nums)
        cache: List[List[int]] = [
            [-1 for _ in range(max_sum + 1)] for _ in range(length + 1)
        ]
        return generate(0, 0, cache)
