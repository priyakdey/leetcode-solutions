"""
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any 
order
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.generate_subsets(nums, 0, [], subsets)
        return subsets

    def generate_subsets(
        self, nums: List[int], index: int, subset: List[int], subsets: List[List[int]]
    ) -> None:
        subsets.append(list(subset))

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.generate_subsets(nums, i + 1, subset, subsets)
            subset.pop()
