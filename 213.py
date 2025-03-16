from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        next_max = nums[-1]
        adjacent_max = nums[-2]

        for i in range(len(nums) - 3, 0, -1):
            curr_max = nums[i] + next_max
            next_max = max(adjacent_max, next_max)
            adjacent_max = curr_max

        max_loot = max(adjacent_max, next_max)

        next_max = nums[-2]
        adjacent_max = nums[-3]

        for i in range(len(nums) - 4, -1, -1):
            curr_max = nums[i] + next_max
            next_max = max(adjacent_max, next_max)
            adjacent_max = curr_max

        return max(adjacent_max, next_max, max_loot)
