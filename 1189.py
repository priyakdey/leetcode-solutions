"""
1189. Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many
instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of
instances that can be formed.
"""

from collections import Counter


INT_MAX = (1 << 31) - 1


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_freq_map = Counter("balloon")
        text_freq_map = Counter(text)

        min_count = INT_MAX
        for ch, freq in balloon_freq_map.items():
            if ch in balloon_freq_map:
                min_count = min(min_count, text_freq_map[ch] // freq)

        return min_count
