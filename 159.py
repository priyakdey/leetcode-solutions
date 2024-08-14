"""
159. Longest Substring with At Most Two Distinct Characters

Given a string s, return the length of the longest substring that contains at
most two distinct characters.
"""
from collections import defaultdict
from typing import Dict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start, curr = 0, 0
        max_length = 0
        freq_count: Dict[str, int] = defaultdict(int)

        while curr < len(s):
            ch = s[curr]
            freq_count[ch] += 1
            if len(freq_count) > 2:
                max_length = max(max_length, curr - 1 - start + 1)
                while len(freq_count) > 2:
                    freq_count[s[start]] -= 1
                    if freq_count[s[start]] == 0:
                        del freq_count[s[start]]
                    start += 1

            curr += 1

        max_length = max(max_length, curr - 1 - start + 1)
        return max_length
