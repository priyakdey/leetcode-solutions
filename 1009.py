"""
1009. Complement of Base 10 Integer

The complement of an integer is the integer you get when you flip all the
0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010"
which is the integer 2.
Given an integer n, return its complement.
"""


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n < 2:
            return n ^ 1

        compliment = 0

        position = 0
        while n > 0:
            bit = (n & 1) ^ 1
            compliment = compliment | (bit << position)
            position += 1
            n = n >> 1

        return compliment
