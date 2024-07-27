"""
1216. Valid Palindrome III

Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing
at most k characters from it.
"""

from typing import Tuple, Dict, List


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def valid(
            left: int, right: int, k: int, cache: Dict[Tuple[int, int, int], bool]
        ) -> bool:
            if left >= right:
                return True

            key = (left, right, k)
            if key in cache:
                return cache[key]

            if s[left] == s[right]:
                return valid(left + 1, right - 1, k, cache)

            if k == 0:
                return False

            is_valid = valid(left + 1, right, k - 1, cache) or valid(
                left, right - 1, k - 1, cache
            )
            cache[key] = is_valid
            return is_valid

        if s is None or len(s) == 0:
            raise Exception("invalid arguments")
        if len(s) == 1:
            return True
        return valid(0, len(s) - 1, k, {})
