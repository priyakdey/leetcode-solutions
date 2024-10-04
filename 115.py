"""
115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s
which equals t.

The test cases are generated so that the answer fits on a 32-bit signed
integer.
"""

from typing import List


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def traverse(s: str, i: int, t: str, j: int, cache: List[List[int]]) -> int:
            if i == len(s):
                return 1 if j == len(t) else 0

            if j == len(t):
                return 1

            if cache[i][j] != -1:
                return cache[i][j]

            if s[i] == t[j]:
                count = traverse(s, i + 1, t, j + 1, cache) + traverse(
                    s, i + 1, t, j, cache
                )
            else:
                count = traverse(s, i + 1, t, j, cache)

            cache[i][j] = count
            return count

        cache: List[List[int]] = [
            [-1 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)
        ]
        return traverse(s, 0, t, 0, cache)
