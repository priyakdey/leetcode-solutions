from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        buf: List[int] = [""] * (len1 + len2)

        i, j, k = 0, 0, 0
        while i < len1 and j < len2:
            buf[k] = word1[i]
            k += 1
            i += 1
            buf[k] = word2[j]
            k += 1
            j += 1

        while i < len1:
            buf[k] = word1[i]
            k += 1
            i += 1

        while j < len2:
            buf[k] = word2[j]
            k += 1
            j += 1

        return "".join(buf)
