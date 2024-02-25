"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last 
word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = 0
        buffer = []
        for ch in s:
            if ch != " ":
                buffer.append(ch)
            else:
                if len(buffer) != 0:
                    last_word_length = len(buffer)
                    buffer = []

        if len(buffer) != 0:
            last_word_length = len(buffer)

        return last_word_length
