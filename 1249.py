"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any 
positions ) so that the resulting parentheses string is valid and return any 
valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
"""

from typing import List


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        intermediate_buffer: List[str] = []
        balanced: int = 0

        for ch in s:
            if ch == ")":
                if balanced > 0:
                    intermediate_buffer.append(ch)
                    balanced -= 1
            else:
                if ch == "(":
                    balanced += 1
                intermediate_buffer.append(ch)

        buffer: List[str] = []
        for i in range(len(intermediate_buffer) - 1, -1, -1):
            ch = intermediate_buffer[i]
            if ch == "(":
                if balanced > 0:
                    balanced -= 1
                else:
                    buffer.insert(0, ch)
            else:
                buffer.insert(0, ch)

        return "".join(buffer)
