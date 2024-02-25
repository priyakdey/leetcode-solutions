"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to 
get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same 
character, but a character may map to itself.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False

        replace_map = dict()
        i = 0
        for i in range(len(s)):
            ch1, ch2 = s[i], t[i]
            if ch1 in replace_map:
                if replace_map[ch1] != ch2:
                    return False
            else:
                if ch2 in replace_map.values():
                    # ch2 is already mapped to a key, we cannot remap
                    return False
                replace_map[ch1] = ch2

        return True
