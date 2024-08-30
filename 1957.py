"""
1957. Delete Characters to Make Fancy String

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to
make it fancy.

Return the final string after the deletion. It can be shown that the answer
will always be unique.
"""

from collections import deque
from typing import Deque


class Solution:
    def makeFancyString(self, s: str) -> str:
        if s is None or len(s) == 0:
            raise Exception("invalid input string")

        if len(s) < 3:
            return s

        stack: Deque[str] = deque()
        stack.append(s[0])
        uniq_ch: str = s[0]
        streak: int = 1

        for i in range(1, len(s)):
            ch = s[i]
            if ch == uniq_ch:
                streak += 1
                if streak < 3:
                    stack.append(ch)
            else:
                uniq_ch = ch
                streak = 1
                stack.append(ch)

        return "".join(stack)
