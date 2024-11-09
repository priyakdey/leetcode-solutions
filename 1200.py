"""
1200. Minimum Absolute Difference

Given an array of distinct integers arr, find all pairs of elements with the
minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair
[a, b] follows

- a, b are from arr
- a < b
- b - a equals to the minimum absolute difference of any two elements in arr
"""

from typing import List


INT_MAX = (1 << 31) - 1


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = INT_MAX

        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        pairs: List[List[int]] = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                pairs.append([arr[i - 1], arr[i]])

        return pairs
