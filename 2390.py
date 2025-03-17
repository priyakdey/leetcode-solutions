from collections import deque
from typing import Deque


class Solution:
    def removeStars(self, s: str) -> str:
        stack: Deque[str] = deque()

        for ch in s:
            if ch == "*":
                assert len(stack) > 0
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
