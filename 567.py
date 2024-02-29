"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or 
false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

from collections import Counter
from typing import Dict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) > len(s2):
            return False

        table1 = Counter(s1)

        k = len(s1)

        table2: Dict[str, int] = {}
        for i in range(k):
            if s2[i] in table2:
                table2[s2[i]] += 1
            else:
                table2[s2[i]] = 1

        if table1 == table2:
            return True

        for i in range(k, len(s2)):
            if s2[i] in table2:
                table2[s2[i]] += 1
            else:
                table2[s2[i]] = 1

            table2[s2[i - k]] -= 1
            if table2[s2[i - k]] == 0:
                del table2[s2[i - k]]

            if table1 == table2:
                return True

        return False
