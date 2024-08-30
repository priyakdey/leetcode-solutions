"""
80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some
duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the
first k elements of nums should hold the final result. It does not matter what
you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying
the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            raise Exception("invalid arguments")

        insert_at, curr = 0, 1
        last_uniq_element = nums[0]
        streak = 1

        while curr < len(nums):
            if nums[curr] != last_uniq_element:
                for i in range(min(2, streak)):
                    nums[insert_at] = last_uniq_element
                    insert_at += 1
                last_uniq_element = nums[curr]
                streak = 0
            curr += 1
            streak += 1

        for i in range(min(2, streak)):
            nums[insert_at] = last_uniq_element
            insert_at += 1
        return insert_at
