"""
245. Shortest Word Distance III

Given an array of strings wordsDict and two strings that already exist in the
array word1 and word2, return the shortest distance between the occurrence of
these two words in the list.

Note that word1 and word2 may be the same. It is guaranteed that they represent
two individual words in the list.
"""

from typing import List


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        def get_indices(word: str) -> List[int]:
            nonlocal wordsDict

            indices: List[int] = []

            for i, _word in enumerate(wordsDict):
                if word == _word:
                    indices.append(i)

            return indices

        min_distance = len(wordsDict)

        if word1 == word2:
            indices = get_indices(word1)

            for i in range(1, len(indices)):
                min_distance = min(min_distance, indices[i] - indices[i - 1])

            min_distance = min(min_distance, abs(indices[0] - indices[-1]))
        else:
            word1_indices = get_indices(word1)
            word2_indices = get_indices(word2)

            i, j = 0, 0
            min_distance = len(wordsDict)

            while i < len(word1_indices) and j < len(word2_indices):
                min_distance = min(
                    min_distance, abs(word1_indices[i] - word2_indices[j])
                )
                if word1_indices[i] < word2_indices[j]:
                    i += 1
                else:
                    j += 1

            min_distance = min(min_distance, abs(word1_indices[0] - word2_indices[-1]))
            min_distance = min(min_distance, abs(word1_indices[-1] - word2_indices[0]))

        return min_distance
