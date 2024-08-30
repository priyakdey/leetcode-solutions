"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to
get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character, but a character may map to itself.
"""

from typing import Dict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False

        s_to_t: Dict[str, str] = {}
        t_to_s: Dict[str, str] = {}

        for i in range(len(s)):
            ch1, ch2 = s[i], t[i]
            if ch1 in s_to_t:
                if s_to_t[ch1] != ch2:
                    return False
            else:
                if ch2 in t_to_s:
                    return False
                s_to_t[ch1] = ch2
                t_to_s[ch2] = ch1

        return True

