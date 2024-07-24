"""
2068. Check Whether Two Strings are Almost Equivalent

Two strings word1 and word2 are considered almost equivalent if the differences
between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

Given two strings word1 and word2, each of length n, return true if word1 and
word2 are almost equivalent, or false otherwise.

The frequency of a letter x is the number of times it occurs in the string.
"""

from typing import List


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq_arr1 = self.to_freq_arr(word1)
        freq_arr2 = self.to_freq_arr(word2)

        for i in range(26):
            if abs(freq_arr1[i] - freq_arr2[i]) > 3:
                return False

        return True

    @staticmethod
    def to_freq_arr(word: str) -> List[int]:
        freq_arr = [0] * 26
        for ch in word:
            freq_arr[ord(ch) - 97] += 1

        return freq_arr
