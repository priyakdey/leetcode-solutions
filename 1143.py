from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        cache: List[List[int]] = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                max_length = max(cache[i][j + 1], cache[i + 1][j])
                if text1[i] == text2[j]:
                    max_length = max(max_length, 1 + cache[i + 1][j + 1])
                cache[i][j] = max_length

        return cache[0][0]
