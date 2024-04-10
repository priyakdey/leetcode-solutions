"""
44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching 
with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).
"""

from typing import List, Optional


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache: List[List[Optional[bool]]] = [
            [None for _ in range(len(p))] for _ in range(len(s))
        ]
        return self.is_match(s, 0, p, 0, cache)

    def is_match(
        self,
        s: str,
        index1: int,
        p: str,
        index2: int,
        cache: List[List[Optional[bool]]],
    ) -> bool:
        if index1 == len(s):
            while index2 < len(p) and p[index2] == "*":
                index2 += 1
            return index2 == len(p)

        if index2 == len(p):
            return False

        if cache[index1][index2] is not None:
            return cache[index1][index2]  # type: ignore

        ch = p[index2]
        is_match_till = False
        match ch:
            case "?":
                is_match_till = self.is_match(s, index1 + 1, p, index2 + 1, cache)
            case "*":
                is_match_till = self.is_match(
                    s, index1 + 1, p, index2, cache
                ) or self.is_match(s, index1, p, index2 + 1, cache)
            case _:
                is_match_till = s[index1] == ch and self.is_match(
                    s, index1 + 1, p, index2 + 1, cache
                )
        cache[index1][index2] = is_match_till
        return is_match_till
