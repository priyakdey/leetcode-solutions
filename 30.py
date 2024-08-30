"""
30. Substring with Concatenation of All Words

You are given a string s and an array of strings words. All the strings of
words are of the same length.

A concatenated string is a string that exactly contains all the strings of
any permutation of words concatenated.

- For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd",
"cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings.
"acdbef" is not a concatenated string because it is not the concatenation of
any permutation of words.

Return an array of the starting indices of all the concatenated substrings in
s. You can return the answer in any order.
"""

from collections import defaultdict
from typing import Dict, List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def to_freq_map(
            s: str, start: int, end: int, word_length: int
        ) -> Dict[str, int]:
            freq_map: Dict[str, int] = defaultdict(int)
            for i in range(start, end, word_length):
                freq_map[s[i : i + word_length]] += 1
            return freq_map

        def is_map_equal(map1: Dict[str, int], map2: Dict[str, int]) -> bool:
            if len(map1) != len(map2):
                return False

            for k, v in map1.items():
                if k not in map2 or map2[k] != v:
                    return False

            return True

        word_length = len(words[0])
        total_length = word_length * len(words)

        word_freq_map = defaultdict(int)
        for word in words:
            word_freq_map[word] += 1

        indices: List[int] = []

        for i in range(len(s) - word_length + 1):
            freq_map = to_freq_map(s, i, i + total_length, word_length)
            if is_map_equal(word_freq_map, freq_map):
                indices.append(i)

        return indices
