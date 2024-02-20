"""
45. Jump Game II

You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from 
index i. In other words, if you are at nums[i], you can jump to any nums[i + j] 
where:

- 0 <= j <= nums[i] and
- i + j < n

Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 1 if nums[0] != -1 else 0

        INT_MAX = (1 << 31) - 1

        jumps: List[int] = [0 for _ in nums]
        jumps[-2] = 1 if nums[-2] != 0 else 0
        for i in range(len(nums) - 3, -1, -1):
            if i + nums[i] >= len(nums) - 1:
                jumps[i] = 1
            else:
                min_jump = INT_MAX
                for j in range(i + 1, i + nums[i] + 1):
                    if jumps[j] != 0:
                        min_jump = min(min_jump, jumps[j])
                jumps[i] = 1 + min_jump if min_jump != INT_MAX else 0

        return jumps[0]
