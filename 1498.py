"""
1498. Number of Subsequences That Satisfy the Given Sum Condition

You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the
minimum and maximum element on it is less or equal to target.
Since the answer may be too large, return it modulo 10^9 + 7.
"""
from typing import List

MOD = 1_000_000_007

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        def find_index(arr: List[int], target: int, start_index) -> int:
            index = -1
            left, right = start_index, len(arr) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] <= target:
                    index = mid
                    left = mid + 1
                else:
                    right = mid - 1

            return index

        nums.sort()
        count = 0

        for i in range(len(nums)):
            index = find_index(nums, target - nums[i], i)
            if index != -1:
                count = (count + (1 << (index - i))) % MOD

        return count
