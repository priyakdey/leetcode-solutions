"""
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression
matching with support for '.' and '*' where:

- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
"""


class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        def is_match(i: int, j: int) -> bool:
            if j < len(pattern) - 1 and pattern[j + 1] == "*":
                return is_match(i, j + 1)
            elif pattern[j] == "*":
                k = i
                while k < len(string) and string[k] == pattern[k - 1]

