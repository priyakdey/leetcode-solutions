"""
2864. Maximum Odd Binary Number

You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number 
is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created 
from the given combination.

Note that the resulting string can have leading zeros.
"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        length = len(s)
        on_count = 0

        for ch in s:
            if ch == "1":
                on_count += 1

        if on_count == 0:
            return s

        buffer = []
        for i in range(on_count - 1):
            buffer.append("1")
        for i in range(length - on_count):
            buffer.append("0")

        buffer.append("1")
        return "".join(buffer)
