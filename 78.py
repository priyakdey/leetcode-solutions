"""
78. Subsets

Given an integer array nums of unique elements, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any 
order.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = []
        self.generate_subset(nums, 0, [], subsets)
        return subsets

    def generate_subset(
        self, nums: List[int], index: int, subset: List[int], subsets: List[List[int]]
    ) -> None:
        if index == len(nums):
            subsets.append(list(subset))
            return

        self.generate_subset(nums, index + 1, subset, subsets)

        subset.append(nums[index])
        self.generate_subset(nums, index + 1, subset, subsets)
        subset.pop()
