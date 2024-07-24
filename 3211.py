"""
3211. Generate Binary Strings Without Adjacent Zeros

You are given a positive integer n.

A binary string x is valid if all substrings of x of length 2 contain at least 
one "1".

Return all valid strings with length n, in any order.
"""

from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n < 1:
            raise Exception("invalid arguments")

        acc: List[str] = []
        self.generate_strings(["0"] * n, 0, n, acc)
        return acc

    def generate_strings(
        self, buf: List[str], index: int, n: int, acc: List[str]
    ) -> None:
        if index == n:
            acc.append("".join(buf))
            return

        if index > 0 and buf[index - 1] == "0":
            buf[index] = "1"
            self.generate_strings(buf, index + 1, n, acc)
        else:
            buf[index] = "0"
            self.generate_strings(buf, index + 1, n, acc)
            buf[index] = "1"
            self.generate_strings(buf, index + 1, n, acc)
