"""
228. Summary Ranges

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the 
array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and 
there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        ranges: List[str] = []

        start = 0
        for curr in range(1, len(nums)):
            if nums[curr] != nums[curr - 1] + 1:
                length = curr - 1 - start + 1
                if length == 1:
                    ranges.append(str(nums[start]))
                else:
                    ranges.append(f"{str(nums[start])}->{str(nums[curr - 1])}")
                start = curr

        length = len(nums) - start
        if length == 1:
            ranges.append(str(nums[start]))
        else:
            ranges.append(f"{str(nums[start])}->{str(nums[-1])}")

        return ranges
