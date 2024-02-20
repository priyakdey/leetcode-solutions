"""
162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is 
always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        left, right = 1, len(nums) - 2
        peak_index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                peak_index = mid
                break
            elif nums[mid] < nums[mid + 1] and nums[mid] > nums[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1

        return peak_index
