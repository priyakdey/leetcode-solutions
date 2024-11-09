"""
2869. Minimum Operations to Collect Elements

You are given an array nums of positive integers and an integer k.

In one operation, you can remove the last element of the array and add it to
your collection.

Return the minimum number of operations needed to collect elements 1, 2, ..., k.
"""
from typing import List, Set


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        distinct: Set[int] = {i for i in range(1, k + 1)}

        curr = len(nums) - 1
        while curr >= 0:
            if len(distinct) == 0:
                break
            if nums[curr] in distinct:
                distinct.remove(nums[curr])
            curr -= 1

        return len(nums) - 1 - curr
