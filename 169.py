"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than [n / 2] times. 
You may assume that the majority element always exists in the array.
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        balance = 1
        for i in range(1, len(nums)):
            num = nums[i]
            if num == majority:
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                majority = num
                balance = 0

        # # second pass to validate
        # not needed in this case with constraints - You may assume that the majority element always exists in the array.
        # count = 0
        # for num in nums:
        #     if num == majority:
        #         count += 1

        # if count < len(nums) // 2:
        #     return -1
        return majority
