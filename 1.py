"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

You can return the answer in any order.
"""

from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = [-1, -1]
        element_index_map: Dict[int, int] = {}

        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in element_index_map:
                indices[0] = element_index_map[compliment]
                indices[1] = index
                break
            element_index_map[num] = index

        return indices
