"""
1413. Minimum Value to Get Positive Step by Step Sum

Given an array of integers nums, you start with an initial positive value
startValue.

In each iteration, you calculate the step by step sum of startValue plus
elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum
is never less than 1.
"""

from typing import List


INT_MAX = (1 << 31) - 1


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = INT_MAX
        curr_sum = 0

        for num in nums:
            curr_sum += num
            min_sum = min(min_sum, curr_sum)

        return 1 - min_sum if min_sum < 1 else 1
