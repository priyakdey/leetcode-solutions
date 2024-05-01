"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating 
characters.
"""

from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index: List[int] = [-1 for i in range(128)]
        start = 0
        max_length = 0
        for i in range(len(s)):
            ch = s[i]
            index = ord(ch)
            if char_index[index] >= start:
                length = i - 1 - start + 1
                max_length = max(max_length, length)
                start = char_index[index] + 1
            char_index[index] = i

        length = len(s) - 1 - start + 1
        max_length = max(max_length, length)

        return max_length
