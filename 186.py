"""
186. Reverse Words in a String II

Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be
separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.
"""
from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left: int, right: int) -> None:
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        reverse(0, len(s) - 1)

        start, curr = 0, 0

        while curr < len(s):
            if s[curr] == " ":
                reverse(start, curr - 1)
                start = curr + 1
            curr += 1

        reverse(start, len(s) - 1)




