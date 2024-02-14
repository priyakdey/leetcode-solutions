"""
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching 
with support for '.' and '*' where:

- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""

# TODO: This does not work yet


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.is_match(s, 0, p, 0)

    def is_match(self, input_str: str, index1: int, pattern: str, index2: int) -> bool:
        if index1 == len(input_str):
            return True

        if index2 == len(pattern):
            return False

        ch = pattern[index2]
        match ch:
            case ".":
                return self.is_match(input_str, index1 + 1, pattern, index2 + 1)
            case "*":
                # iterate over till mismatch
                preceding_ch = pattern[index2 - 1]
                while index1 < len(input_str) and (
                    input_str[index1] == preceding_ch or preceding_ch == "."
                ):
                    index1 += 1
                return self.is_match(input_str, index1, pattern, index2 + 1)
            case _:
                if index2 < len(pattern) - 1 and pattern[index2 + 1] == "*":
                    return self.is_match(input_str, index1, pattern, index2 + 1)
                else:
                    return input_str[index1] == ch and self.is_match(
                        input_str, index1 + 1, pattern, index2 + 1
                    )
