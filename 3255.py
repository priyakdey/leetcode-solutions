"""
325. Find the Power of K-Size Subarrays II

You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

- Its maximum element if all of its elements are consecutive and sorted in
  ascending order.
- -1 otherwise.

You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the
power of nums[i..(i + k - 1)].
"""

from typing import List, Tuple


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        powers: List[int] = [-1] * (length - k + 1)

        streak_indices: List[Tuple[int, int]] = []
        start = 0
        for i in range(1, length):
            if nums[i] != nums[i - 1] + 1:
                streak_indices.append((start, i - 1))
                start = i

        streak_indices.append((start, length - 1))
        # print(streak_indices)

        curr = 0
        for i in range(length - k + 1):
            if i > streak_indices[curr][1]:
                curr += 1

            if i + k <= streak_indices[curr][1]:
                powers[curr] = nums[i + k - 1]
            else:
                powers[i] = -1

        return powers
