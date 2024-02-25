"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.
"""

from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count_map: Dict[str, int] = {}
        for ch in s:
            if ch in char_count_map:
                char_count_map[ch] += 1
            else:
                char_count_map[ch] = 1

        is_anagram = True
        for ch in t:
            if ch not in char_count_map:
                is_anagram = False
                break
            char_count_map[ch] -= 1
            if char_count_map[ch] == 0:
                del char_count_map[ch]

        return is_anagram
