"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: List[List[int]] = []
        self.generate_permutations(nums, 0, permutations)
        return permutations

    def generate_permutations(
        self, nums: List[int], index: int, permutations: List[List[int]]
    ) -> None:
        if index == len(nums):
            permutations.append(list(nums))
            return

        self.generate_permutations(nums, index + 1, permutations)

        for i in range(index + 1, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.generate_permutations(nums, index + 1, permutations)
            nums[index], nums[i] = nums[i], nums[index]
