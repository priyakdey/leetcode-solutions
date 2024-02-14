"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

from collections import deque
from typing import Deque


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}

        is_valid = True
        stack: Deque[str] = deque()
        for bracket in s:
            if bracket in bracket_map:
                if len(stack) == 0 or stack.pop() != bracket_map[bracket]:
                    return False
            else:
                stack.append(bracket)

        return len(stack) == 0
