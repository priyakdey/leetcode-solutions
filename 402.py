"""
402. Remove K Digits

Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.
"""

from collections import deque
from typing import Deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"

        stack: Deque[str] = deque()

        for ch in num:
            while len(stack) != 0 and stack[-1] > ch and k > 0:
                stack.pop()
                k -= 1
            stack.append(ch)

        # remove from end, stack is already lowest number possible but k != 0
        while len(stack) != 0 and k > 0:
            stack.pop()
            k -= 1

        # remove leading zeros except the number "0"
        while len(stack) != 1 and stack[0] == "0":
            stack.popleft()

        return "".join(stack)
