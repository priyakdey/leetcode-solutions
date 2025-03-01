"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        index_of = -1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                index_of = mid
                break
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return index_of
