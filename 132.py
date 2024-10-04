"""
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a
palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.
"""

from typing import List, Optional


INT_MAX = (1 << 31) - 1


class Solution:
    def minCut(self, s: str) -> int:
        def is_palindrome(start: int, end: int) -> bool:
            nonlocal s

            left, right = start, end - 1
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1

            return left >= right

        def partition(start: int, end: int, cache: List[List[Optional[int]]]) -> int:
            nonlocal s

            if end == len(s):
                return 0 if is_palindrome(start, end) else INT_MAX

            if cache[start][end] is not None:
                return cache[start][end]

            # do not partition
            cuts = partition(start, end + 1, cache)

            if is_palindrome(start, end):
                c = partition(end, end + 1, cache)
                if c != INT_MAX:
                    cuts = min(cuts, 1 + c)

            cache[start][end] = cuts
            return cuts

        length = len(s)
        cache: List[List[Optional[int]]] = [
            [None for _ in range(length + 1)] for _ in range(length + 1)
        ]
        min_cuts = partition(0, 1, cache)
        return min_cuts if min_cuts != INT_MAX else length - 1
