"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest 
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

from typing import List, Set


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        max_streak = 0
        visited: Set[int] = set(nums)

        for num in nums:
            if num in visited:
                visited.remove(num)

                left = num - 1
                while left in visited:
                    visited.remove(left)
                    left -= 1

                right = num + 1
                while right in visited:
                    visited.remove(right)
                    right += 1

                max_streak = max(max_streak, (right - 1) - (left + 1) + 1)

        return max_streak
