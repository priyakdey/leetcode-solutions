"""
405. Convert a Number to Hexadecimal

Given a 32-bit integer num, return a string representing its hexadecimal
representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there
should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve
this problem.
"""

from typing import List


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_mapping: str = "0123456789abcdef"

        buf: List[str] = [""] * 8

        for i in range(7, -1, -1):
            buf[i] = hex_mapping[num & 0xF]
            num = num >> 4

        curr = 0
        while curr < len(buf) and buf[curr] == "0":
            curr += 1

        return "".join(buf[curr:])
