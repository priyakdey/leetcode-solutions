"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >= 0 and x <= 9:
            return True

        reverse = 0
        temp = x
        while temp != 0:
            unit = temp % 10
            reverse = reverse * 10 + unit
            temp = temp // 10

        return x == reverse
