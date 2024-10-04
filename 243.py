"""
243. Shortest Word Distance

Given an array of strings wordsDict and two different strings that already
exist in the array word1 and word2, return the shortest distance between these
two words in the list.
"""

from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        def get_indices(word: str) -> List[int]:
            nonlocal wordsDict

            indices: List[int] = []

            for i, _word in enumerate(wordsDict):
                if word == _word:
                    indices.append(i)

            return indices

        word1_indices = get_indices(word1)
        word2_indices = get_indices(word2)

        i, j = 0, 0
        min_distance = len(wordsDict)

        while i < len(word1_indices) and j < len(word2_indices):
            min_distance = min(min_distance, abs(word1_indices[i] - word2_indices[j]))
            if word1_indices[i] < word2_indices[j]:
                i += 1
            else:
                j += 1

        min_distance = min(min_distance, abs(word1_indices[0] - word2_indices[-1]))
        min_distance = min(min_distance, abs(word1_indices[-1] - word2_indices[0]))
        return min_distance
