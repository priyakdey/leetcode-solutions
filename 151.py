"""
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between 
two words. The returned string should only have a single space separating the 
words. Do not include any extra spaces.
"""

from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        buffer: List[str] = []
        buf0: List[str] = []

        for ch in s:
            if ch == " ":
                if len(buf0) != 0:
                    buffer.insert(0, "".join(buf0))
                    buf0.clear()
            else:
                buf0.append(ch)

        if len(buf0) != 0:
            buffer.insert(0, "".join(buf0))

        return " ".join(buffer)
