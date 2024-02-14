"""
97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of 
s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are 
divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm

|n - m| <= 1

The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or 
t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

"""

from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def _is_interleave(index1: int, index2: int, index3: int) -> bool:
            if index1 == len(s1) and index2 == len(s2):
                return index3 == len(s3)
            if index1 == len(s1):
                return s2[index2:] == s3[index3:]
            if index2 == len(s2):
                return s1[index1:] == s3[index3:]

            if cache[index1][index2][index3] is not None:
                return cache[index1][index2][index3]

            is_interleaving = False

            if s1[index1] == s3[index3]:
                is_interleaving = is_interleaving or _is_interleave(
                    index1 + 1, index2, index3 + 1
                )
            if s2[index2] == s3[index3]:
                is_interleaving = is_interleaving or _is_interleave(
                    index1, index2 + 1, index3 + 1
                )

            cache[index1][index2][index3] = is_interleaving
            return is_interleaving

        if len(s1) + len(s2) != len(s3):
            return False

        cache: List[List[List[bool]]] = [
            [[None for _ in range(len(s3) + 1)] for _ in range(len(s2) + 1)]
            for _ in range(len(s1) + 1)
        ]  # type: ignore
        return _is_interleave(0, 0, 0)
