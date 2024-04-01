"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last 
word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        current_length = 0
        for ch in s:
            if ch.isspace():
                if current_length != 0:
                    length = current_length
                current_length = 0
            else:
                current_length += 1
        
        if current_length != 0:
            length = current_length
        
        return length

