from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1, length2 = len(word1), len(word2)
        cache = [[-1 for _ in range(length2 + 1)] for _ in range(length1 + 1)]
        return self.calc_lev(word1, length1 - 1, word2, length2 - 1, cache)

    def calc_lev(
        self, word1: str, index1: int, word2: str, index2: int, cache: List[List[int]]
    ) -> int:
        if index1 == -1:
            return index2 - 0 + 1
        if index2 == -1:
            return index1 - 0 + 1

        if cache[index1][index2] != -1:
            return cache[index1][index2]

        if word1[index1] == word2[index2]:
            return self.calc_lev(word1, index1 - 1, word2, index2 - 1, cache)

        lev_dist = 1 + min(
            self.calc_lev(word1, index1 - 1, word2, index2, cache),
            self.calc_lev(word1, index1, word2, index2 - 1, cache),
            self.calc_lev(word1, index1 - 1, word2, index2 - 1, cache),
        )
        cache[index1][index2] = lev_dist
        return lev_dist
