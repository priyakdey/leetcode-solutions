"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""

from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s is None or len(s) == 0:
            raise Exception("invalid input")

        if len(s) <= 1:
            return len(s)

        char_freq: List[int] = [0 for i in range(52)]
        for ch in s:
            index = self.__index(ch)
            char_freq[index] += 1

        is_odd_present = False
        length = 0
        for freq in char_freq:
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                is_odd_present = True

        if is_odd_present:
            length += 1
        return length

    def __index(self, ch: str) -> int:
        """
        65 - 90  -> 0  - 25
        97 - 122 -> 26 - 51
        """
        if ch.isupper():
            return ord(ch) - 65
        else:
            return ord(ch) - 71
