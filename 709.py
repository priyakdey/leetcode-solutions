"""
709. To Lower Case

Given a string s, return the string after replacing every uppercase letter with
the same lowercase letter.
"""
from typing import List


class Solution:
    def toLowerCase(self, s: str) -> str:
        buf: List[str] = [""] * len(s)
        for i, ch in enumerate(s):
            if 65 <= ord(ch) <= 90:
                buf[i] = chr(ord(ch) ^ 32)
            else:
                buf[i] = ch

        return "".join(buf)
