"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward 
and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # fmt: off
        valid_charset = \
        {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', 
         '2', '3', '4', '5', '6', '7', '8', '9'}
        # fmt: on

        left, right = 0, len(s) - 1
        is_palindrome = True

        copy = s.lower()

        while left < right:
            if copy[left] not in valid_charset and copy[right] not in valid_charset:
                left += 1
                right -= 1
            elif copy[left] not in valid_charset and copy[right] in valid_charset:
                left += 1
            elif copy[left] in valid_charset and copy[right] not in valid_charset:
                right -= 1
            else:
                if copy[left] != copy[right]:
                    is_palindrome = False
                    break
                left += 1
                right -= 1

        return is_palindrome
