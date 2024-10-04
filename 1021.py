"""
1021. Remove Outermost Parentheses

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where
A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses
strings.
A valid parentheses string s is primitive if it is nonempty, and there does
not exist a way to split it into s = A + B, with A and B nonempty valid
parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition:
s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string
in the primitive decomposition of s.
"""

from collections import deque
from typing import Deque, List, Set, Tuple


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack: Deque[Tuple[str, int]] = deque()

        remove: Set[int] = set()

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append((ch, i))
            else:
                _, index = stack.pop()
                if i - index > 1:
                    remove.add(i)

        buf: List[str] = []
        for i, ch in enumerate(s):
            if i not in remove:
                buf.append(ch)

        return "".join(buf)
