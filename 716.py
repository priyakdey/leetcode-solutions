"""
716. Max Stack

Design a max stack data structure that supports the stack operations and 
supports finding the stack's maximum element.

Implement the MaxStack class:

- MaxStack() Initializes the stack object.
- void push(int x) Pushes element x onto the stack.
- int pop() Removes the element on top of the stack and returns it.
- int top() Gets the element on the top of the stack without removing it.
- int peekMax() Retrieves the maximum element in the stack without removing it.
- int popMax() Retrieves the maximum element in the stack and removes it. 
  If there is more than one maximum element, only remove the top-most one.

You must come up with a solution that supports O(1) for each top call 
and O(logn) for each other call.
"""

from collections import deque
from typing import Deque, Tuple


class MaxStack:

    def __init__(self):
        self.stack: Deque[Tuple[int, int]] = deque()

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            self.stack.append((x, max(self.peekMax(), x)))

    def pop(self) -> int:
        if len(self.stack) == 0:
            raise Exception("underflow")
        return self.stack.pop()[0]

    def top(self) -> int:
        if len(self.stack) == 0:
            raise Exception("underflow")
        return self.stack[-1][0]

    def peekMax(self) -> int:
        if len(self.stack) == 0:
            raise Exception("underflow")
        return self.stack[-1][1]

    def popMax(self) -> int:
        if len(self.stack) == 0:
            raise Exception("underflow")
        return self.stack.pop()[1]
