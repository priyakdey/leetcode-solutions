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
            if j == len(pattern):
                return i == len(string)

            match = i < len(string) and (string[i] == pattern[j] or pattern[j] == ".")

            if j < len(pattern) - 1 and pattern[j + 1] == "*":
                match = is_match(i, j + 2) or (match and is_match(i + 1, j))
            else:
                match = match and is_match(i + 1, j + 1)

            return match

        return is_match(0, 0)
