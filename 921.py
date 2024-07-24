"""
921. Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:
- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid
  strings, or
- It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a
parenthesis at any position of the string.
- For example, if s = "()))", you can insert an opening parenthesis to be
  "(()))" or a closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid.
"""

from collections import deque
from typing import Deque


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s is None or len(s) == 0:
            raise Exception("invalid input")

        stack: Deque[str] = deque()
        insert = 0
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    insert += 1
                else:
                    stack.pop()

        return insert + len(stack)
