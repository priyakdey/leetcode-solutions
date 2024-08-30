"""
137. Single Number II

Given an integer array nums where every element appears three times except for
one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only
constant extra space.
"""

from typing import List

INT_MAX = 1 << 31

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = 0

        for i in range(32):
            total = 0
            for num in nums:
                total += (num >> i) & 1

            bit = total % 3
            single_number = single_number | (bit << i)

        if single_number >= INT_MAX:
            single_number = -((INT_MAX << 1) - single_number)

        return single_number
