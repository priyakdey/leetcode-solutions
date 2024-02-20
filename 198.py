"""
198. House Robber

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping 
you from robbing each of them is that adjacent houses have security systems 
connected and it will automatically contact the police if two adjacent houses 
were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the 
police.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        next_max_loot, next_loot = nums[-1], nums[-2]

        for i in range(len(nums) - 3, -1, -1):
            curr_loot = nums[i] + next_max_loot
            next_max_loot = max(next_max_loot, next_loot)
            next_loot = curr_loot

        return max(next_loot, next_max_loot)
