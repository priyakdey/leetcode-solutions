"""
1150. Check If a Number Is Majority Element in a Sorted Array

Given an integer array nums sorted in non-decreasing order and an integer target,
return true if target is a majority element, or false otherwise.

A majority element in an array nums is an element that appears more than
nums.length / 2 times in the array.
"""

from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        start_index = self.find_index(nums, target)
        if start_index == -1:
            return False

        end_index = self.find_index(nums, target + 1)
        if end_index == -1:
            end_index = len(nums) - 1
        else:
            end_index -= 1
        return end_index - start_index + 1 > len(nums) // 2

    @staticmethod
    def find_index(nums: List[int], target: int) -> int:
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
