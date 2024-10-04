"""
89. Gray Code

An n-bit gray code sequence is a sequence of 2^n integers where:

Every integer is in the inclusive range [0, 2^n - 1],
- The first integer is 0,
- An integer appears no more than once in the sequence,
- The binary representation of every pair of adjacent integers differs by
  exactly one bit, and
- The binary representation of the first and last integers differs by exactly
  one bit.

Given an integer n, return any valid n-bit gray code sequence.
"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        seq: List[int] = [0] * (2 ** n)

        for shift in range(n):
            count = 0
            bit = 0
            for i in range(len(seq)):
                seq[i] = seq[i] | (bit << shift)
                count += 1
                if count == 1 << (shift + 1):
                    count = 0
                elif count == 1 << shift:
                    bit = bit ^ 1

        return seq

