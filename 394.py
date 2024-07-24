"""
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the 
square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra 
white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits 
and that digits are only for those repeat numbers, k. For example, 
there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never 
exceed 10^5.
"""

from collections import deque
from typing import List, Deque


class Solution:
    def decodeString(self, s: str) -> str:
        stack: Deque[str] = deque()
        buf: List[str] = []

        for ch in s:
            if ch == "]":
                while len(stack) != 0 and stack[-1] != "[":
                    buf.insert(0, stack.pop())

                stack.pop()  # remove the [
                repeat = 0
                unit = 0
                while len(stack) != 0 and stack[-1].isdigit():
                    repeat += (10**unit) * int(stack.pop())
                    unit += 1
                stack.append("".join(buf * repeat))
                buf.clear()
            else:
                stack.append(ch)

        return "".join(stack)
