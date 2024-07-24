"""
2340. Minimum Adjacent Swaps to Make a Valid Array

You are given a 0-indexed integer array nums.

Swaps of adjacent elements are able to be performed on nums.

A valid array meets the following conditions:

The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
Return the minimum swaps required to make nums a valid array.
"""

from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        max_index = 0
        for i, num in enumerate(nums):
            if num >= nums[max_index]:
                max_index = i

        swaps = len(nums) - 1 - max_index
        max_element = nums[max_index]
        for i in range(max_index + 1, len(nums)):
            nums[i - 1] = nums[i]

        nums[-1] = max_element

        min_index = 0
        for i, num in enumerate(nums):
            if num < nums[min_index]:
                min_index = i

        swaps += min_index
        return swaps
