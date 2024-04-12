"""
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each 
i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        if n == 2:
            return [0, 1, 1]

        set_bit_count = [0 for _ in range(n + 1)]

        set_bit_count[0] = 0
        set_bit_count[1] = 1
        set_bit_count[2] = 1

        for i in range(3, n + 1):
            set_bit_count[i] = set_bit_count[i >> 1]
            if i % 2 != 0:
                set_bit_count[i] += 1

        return set_bit_count
