"""
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most 
one character from it.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(left: int, right: int, can_delete: bool) -> bool:
            if left >= right:
                return True

            if s[left] == s[right]:
                return valid(left + 1, right - 1, can_delete)

            if not can_delete:
                return False

            return valid(left + 1, right, False) or valid(left, right - 1, False)

        if s is None or len(s) == 0:
            raise Exception("invalid arguments")
        if len(s) < 3:
            return True
        return valid(0, len(s) - 1, True)
