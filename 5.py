"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

from typing import Tuple


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        longest_palindrome = ""

        def expand(left: int, right: int) -> Tuple[int, int]:
            """left and right are both inclusive and returns
            the indices for which substring is palindrome
            """

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return (left + 1, right - 1)

        for i in range(len(s)):
            # palindrome is odd length
            left, right = expand(i, i)
            length = right - left + 1
            if length > max_length:
                max_length = length
                longest_palindrome = s[left : right + 1]

            # palindrome is even length
            left, right = expand(i, i + 1)
            length = right - left + 1
            if length > max_length:
                max_length = length
                longest_palindrome = s[left : right + 1]

        return longest_palindrome
