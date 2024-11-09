"""
2595. Number of Even and Odd Bits

You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n
with value 1.

Let odd denote the number of odd indices in the binary representation of n with
value 1.

Note that bits are indexed from right to left in the binary representation of a
number.

Return the array [even, odd].
"""
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0

        for i in range(32):
            bit = (n >> i) & 0x1
            if i % 2 == 0:
                even += bit
            else:
                odd += bit

        return [even, odd]

