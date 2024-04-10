"""
442. Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in 
the range [1, n] and each integer appears once or twice, return an array of 
all the integers that appears twice.


You must write an algorithm that runs in O(n) time and uses only constant 
extra space.
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates: List[int] = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                duplicates.append(num)
            else:
                nums[num - 1] *= -1

        return duplicates
