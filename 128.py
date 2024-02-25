"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest 
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        max_streak = 0
        num_set = set()

        for num in nums:
            num_set.add(num)

        for num in nums:
            if num - 1 not in num_set:
                curr_num = num
                streak = 0
                while curr_num in num_set:
                    streak += 1
                    curr_num += 1
                max_streak = max(max_streak, streak)

        return max_streak
