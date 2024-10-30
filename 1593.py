"""
1593. Split a String Into the Max Number of Unique Substrings

Given a string s, return the maximum number of unique substrings that the
given string can be split into.

You can split string s into any list of non-empty substrings, where the
concatenation of the substrings forms the original string.
However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.
"""

from typing import Set


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def split(start_index: int, end_index: int, substrings: Set[str]) -> int:
            nonlocal s

            substring = s[start_index:end_index]

            if end_index == len(s):
                return 1 if substring not in substrings else 0

            count = split(start_index, end_index + 1, substrings)

            if substring not in substrings:
                substrings.add(substring)
                count = max(count, 1 + split(end_index, end_index + 1, substrings))
                substrings.remove(substring)

            return count

        return split(0, 1, set())
