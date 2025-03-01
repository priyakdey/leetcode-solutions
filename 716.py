# https://leetcode.com/problems/max-stack/
from collections import deque
from typing import Deque


class MaxStack:

    def __init__(self):
        self.stack: Deque[int] = deque()
        self.max: Deque[int] = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.max) == 0 or x >= self.max[-1]:
            self.max.append(x)

    def pop(self) -> int:
        top = self.stack.pop()
        if top == self.max[-1]:
            self.max.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max[-1]

    def popMax(self) -> int:
        temp: Deque[int] = deque()
        max = self.max.pop()
        while self.stack[-1] != max:
            temp.append(self.stack.pop())

        self.stack.pop()

        while len(temp) != 0:
            self.stack.append(temp.pop())

        return max
