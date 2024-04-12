"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters 
in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end 
of the merged string.

Return the merged string.
"""

from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if word1 is None or len(word1) == 0:
            return word2
        if word2 is None or len(word2) == 0:
            return word1

        len1, len2 = len(word1), len(word2)

        buffer: List[str] = ["" for _ in range(len1 + len2)]
        cursor = 0

        i, j = 0, 0

        while i < len1 and j < len2:
            buffer[cursor] = word1[i]
            cursor += 1
            i += 1

            buffer[cursor] = word2[j]
            cursor += 1
            j += 1

        while i < len1:
            buffer[cursor] = word1[i]
            cursor += 1
            i += 1

        while j < len2:
            buffer[cursor] = word2[j]
            cursor += 1
            j += 1

        return "".join(buffer)
