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

        start, end = nums[0], nums[0]
        ranges = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                end = nums[i]
                continue
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(end))
                start, end = nums[i], nums[i]

        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(end))

        return ranges
