"""
540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element 
appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) % 2 == 0:
            raise Exception("invalid argument")

        left, right = 0, len(nums) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2

            if left == right:
                index = left
                break

            if mid & 1 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 1
                else:
                    index = mid
                    right = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    index = mid
                    right = mid - 1

        return nums[index]
