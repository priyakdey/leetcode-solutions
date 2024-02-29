"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of 
the longest valid (well-formed) parentheses substring
"""

from typing import Dict


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_length = 0

        # iterate forward
        weight: Dict[str, int] = {"(": 1, ")": -1}
        start = 0
        balance = 0

        for i, ch in enumerate(s):
            balance += weight[ch]
            if balance == 0:
                max_length = max(max_length, i - start + 1)
            elif balance < 0:
                start = i + 1
                balance = 0

        # iterate backward with opposite weightage
        weight: Dict[str, int] = {"(": -1, ")": 1}
        end = len(s) - 1
        balance = 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            balance += weight[ch]
            if balance == 0:
                max_length = max(max_length, end - i + 1)
            elif balance < 0:
                end = i - 1
                balance = 0

        return max_length
