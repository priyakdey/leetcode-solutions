"""
163. Missing Ranges

You are given an inclusive range [lower, upper] and a sorted unique integer 
array nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is 
not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. 
That is, no element of nums is included in any of the ranges, and each missing 
number is covered by one of the ranges.
"""

from typing import List, Set


class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        missing_ranges: List[List[int]] = []
        distinct: Set[int] = set(nums)

        lower_range = lower
        while lower_range <= upper:
            if lower_range not in nums:
                upper_range = lower_range
                while upper_range not in distinct and upper_range <= upper:
                    upper_range += 1
                missing_ranges.append([lower_range, upper_range - 1])
                lower_range = upper_range
            lower_range += 1

        return missing_ranges
