"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.
"""

from typing import List, Tuple


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"

        buffer: List[str] = []
        i, j = len(a) - 1, len(b) - 1

        carry = "0"

        while i >= 0 and j >= 0:
            carry, bit = self.add(a[i], b[j], carry)
            buffer.append(bit)
            i -= 1
            j -= 1

        while i >= 0:
            carry, bit = self.add(a[i], "0", carry)
            buffer.append(bit)
            i -= 1

        while j >= 0:
            carry, bit = self.add("0", b[j], carry)
            buffer.append(bit)
            j -= 1

        if carry == "1":
            buffer.append(carry)
        # remove trailing zeros
        i = len(buffer) - 1
        while i >= 0 and buffer[i] == "0":
            i -= 1

        buffer = buffer[: i + 1][::-1]
        return "".join(buffer)

    def add(self, a: str, b: str, c: str) -> Tuple[str, str]:
        if a == "0" and b == "0" and c == "0":
            return "0", "0"
        if a == "0" and b == "0" and c == "1":
            return "0", "1"
        if a == "0" and b == "1" and c == "0":
            return "0", "1"
        if a == "0" and b == "1" and c == "1":
            return "1", "0"
        if a == "1" and b == "0" and c == "0":
            return "0", "1"
        if a == "1" and b == "0" and c == "1":
            return "1", "0"
        if a == "1" and b == "1" and c == "0":
            return "1", "0"
        if a == "1" and b == "1" and c == "1":
            return "1", "1"
        raise Exception("invalid input")
