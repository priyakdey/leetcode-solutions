"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their 
longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string 
with some characters (can be none) deleted without changing the relative order 
of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both 
strings.
"""

from typing import List, Optional, cast


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # cache: List[List[Optional[int]]] = [
        #     [None for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)
        # ]
        # return self.longest_common_subsequence(text1, 0, text2, 0, cache)
        return self.longest_common_subsequence_tabular(text1, text2)

    def longest_common_subsequence_tabular(self, text1: str, text2: str) -> int:
        cache: List[List[int]] = [
            [0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)
        ]

        for index1 in range(len(text1) - 1, -1, -1):
            for index2 in range(len(text2) - 1, -1, -1):
                max_length = 0
                if text1[index1] == text2[index2]:
                    max_length = max(max_length, 1 + cache[index1 + 1][index2 + 1])
                max_length = max(
                    max_length,
                    cache[index1 + 1][index2],
                    cache[index1][index2 + 1],
                )
                cache[index1][index2] = max_length

        return cache[0][0]

    def longest_common_subsequence(
        self,
        text1: str,
        index1: int,
        text2: str,
        index2: int,
        cache: List[List[Optional[int]]],
    ) -> int:
        if index1 == len(text1) or index2 == len(text2):
            return 0

        if cache[index1][index2] is not None:
            return cast(int, cache[index1][index2])

        max_length = 0

        if text1[index1] == text2[index2]:
            max_length = 1 + self.longest_common_subsequence(
                text1, index1 + 1, text2, index2 + 1, cache
            )

        max_length = max(
            max_length,
            self.longest_common_subsequence(text1, index1 + 1, text2, index2, cache),
            self.longest_common_subsequence(text1, index1, text2, index2 + 1, cache),
        )

        cache[index1][index2] = max_length
        return max_length
