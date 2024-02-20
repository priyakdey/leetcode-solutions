"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_index = self.find_index(nums, target)
        if start_index == -1:
            # target is not found in the arr
            return [-1, -1]

        if nums[start_index] != target:
            # start_index is not target, but target + delta, so array has no target elements
            return [-1, -1]

        right_index = self.find_index(nums, target + 1)
        if right_index == -1:
            # no element found which is gt target, hence last element has to be target
            return [start_index, len(nums) - 1]

        return [start_index, right_index - 1]

    def find_index(self, nums: List[int], target: int) -> int:
        """Returns the left most index of the target, if target is present.
        If target is not present, it returns the left most index of the next
        greater element.
        If no target or element greater than target found, returns -1.
        """

        index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        return index
