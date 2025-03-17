from collections import deque
from typing import Deque


class Solution:
    def decodeString(self, s: str) -> str:
        def reverse(arr: List[str]) -> List[str]:
            left, right = 0, len(arr) - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

            return arr

        stack: Deque[str] = deque()
        temp_buf: List[str] = []

        for ch in s:
            if ch == "]":
                # pop things till we find the opening pair [
                while len(stack) > 0 and stack[-1] != "[":
                    temp_buf.append(stack.pop())

                assert len(stack) != 0

                word = "".join(reverse(temp_buf))
                temp_buf.clear()
                # pop the opening pair
                stack.pop()

                # pop till we can get digits
                while len(stack) > 0 and stack[-1].isdigit():
                    temp_buf.append(stack.pop())
                k = int("".join(reverse(temp_buf)))
                temp_buf.clear()

                for i in range(k):
                    stack.append(word)

            else:
                stack.append(ch)

        return "".join(stack)
