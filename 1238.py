"""
1238. Circular Permutation in Binary Representation

Given 2 integers n and start. Your task is return any permutation p of (0,1,
2.....,2^n -1) such that :

- p[0] = start
- p[i] and p[i+1] differ by only one bit in their binary representation.
- p[0] and p[2^n -1] must also differ by only one bit in their binary
  representation.
"""

from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        result: List[int] = []
        for i in range(1 << n):
            result.append(start ^ i ^ (i >> 1))

        return result