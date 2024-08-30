"""
611. Valid Triangle Number

Given an integer array nums, return the number of triplets chosen from the
array that can make triangles if we take them as side lengths of a triangle.
"""
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                value = nums[i] + nums[j]
                left, right = j + 1, len(nums) - 1
                index = -1
                while left <= right:
                    mid = left + (right - left) // 2
                    if nums[mid] < value:
                        index = mid
                        left = mid + 1
                    else:
                        right = mid - 1

                if index != -1:
                    count += index - (j + 1) + 1

        return count