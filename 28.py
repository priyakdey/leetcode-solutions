"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence 
of needle in haystack, or -1 if needle is not part of haystack.
"""

# @TODO: This can be done better with KMP and Z-Algorithm


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if len(needle) == len(haystack):
            return 0 if needle == haystack else -1

        start = 0
        end = start + len(needle)

        while end <= len(haystack):
            if haystack[start] == needle[0]:
                if haystack[start:end] == needle:
                    return start
            start += 1
            end += 1

        return -1
