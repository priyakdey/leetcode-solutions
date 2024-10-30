"""
266. Palindrome Permutation

Given a string s, return true if a permutation of the string could form a
palindrome and false otherwise.
"""
from typing import List


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq_map: List[int] = [0] * 26

        for ch in s:
            freq_map[ord(ch) - ord('a')] += 1

        odd_count = 0
        for freq in freq_map:
            if freq % 2 != 0:
                odd_count += 1

        return odd_count < 2