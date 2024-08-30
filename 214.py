"""
214. Shortest Palindrome

You are given a string s. You can convert s to a palindrome by adding
characters in front of it.

Return the shortest palindrome you can find by performing this transformation.
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def is_palindrome(right: int) -> bool:
            left = 0
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1
            return left >= right

        index = -1
        for right in range(len(s) - 1, -1, -1):
            if is_palindrome(right):
                index = right
                break

        return s[len(s) - 1 : index : -1] + s
