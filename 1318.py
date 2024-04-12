"""
1318. Minimum Flips to Make a OR b Equal to c

Given 3 positives numbers a, b and c. Return the minimum flips required in some 
bits of a and b to make ( a OR b == c ). (bitwise OR operation).

Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 
in their binary representation.
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        min_flips = 0

        for i in range(32):
            aBit, bBit, cBit = a & 1, b & 1, c & 1
            if cBit == 1:
                if aBit == 0 and bBit == 0:
                    min_flips += 1
            else:
                if aBit == 1:
                    min_flips += 1
                if bBit == 1:
                    min_flips += 1

            a = a >> 1
            b = b >> 1
            c = c >> 1

        return min_flips
