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
        missing: List[int] = []

        for num in range(lower, upper + 1):
            if num not in nums:
                missing.append(num)

        missing_ranges: List[List[int]] = []
        if len(missing) == 0:
            return missing_ranges

        start = missing[0]
        for i in range(1, len(missing)):
            if missing[i] != missing[i - 1] + 1:
                missing_ranges.append([start, missing[i - 1]])
                start = missing[i]

        missing_ranges.append([start, missing[-1] + 1])
        return missing_ranges
