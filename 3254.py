"""
3254. Find the Power of K-Size Subarrays I

You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

- Its maximum element if all of its elements are consecutive and sorted in
  ascending order.
- -1 otherwise.

You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the
power of nums[i..(i + k - 1)].
"""

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        powers: List[int] = [-1] * (length - k + 1)

        for i in range(length - k + 1):
            power = nums[i + k - 1]
            for j in range(i + 1, i + k):
                if nums[j] != nums[j - 1] + 1:
                    power = -1
                    break

            powers[i] = power

        return powers
