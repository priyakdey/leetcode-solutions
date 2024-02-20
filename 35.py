"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        left, right = 0, len(nums) - 1
        insert_at = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                insert_at = mid
                right = mid - 1
            else:
                left = mid + 1

        return insert_at
