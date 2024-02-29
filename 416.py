"""
416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into 
two subsets such that the sum of the elements in both subsets is equal or 
false otherwise.
"""

from typing import List, Optional, cast


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        cache: List[List[Optional[bool]]] = [
            [None for _ in range(total_sum + 1)] for _ in range(len(nums))
        ]
        return self.can_partition(nums, 0, 0, sum(nums), cache)

    def can_partition(
        self,
        nums: List[int],
        index: int,
        curr_sum: int,
        total_sum: int,
        cache: List[List[Optional[bool]]],
    ) -> bool:
        if index == len(nums):
            return False
        if cache[index][curr_sum] is not None:
            return cast(bool, cache[index][curr_sum])

        if curr_sum == total_sum // 2:
            return True

        result = self.can_partition(
            nums, index + 1, curr_sum, total_sum, cache
        ) or self.can_partition(
            nums, index + 1, curr_sum + nums[index], total_sum, cache
        )
        cache[index][curr_sum] = result
        return result
