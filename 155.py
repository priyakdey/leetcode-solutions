"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element 
in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""

from typing import List, Tuple


class MinStack:

    def __init__(self):
        self.data: List[Tuple[int, int]] = []

    def push(self, val: int) -> None:
        if self.__is_empty():
            self.data.append((val, val))
            return
        curr_min = min(self.getMin(), val)
        self.data.append((val, curr_min))

    def pop(self) -> None:
        if not self.__is_empty():
            self.data.pop(-1)

    def top(self) -> int:
        if self.__is_empty():
            return -1
        return self.data[-1][0]

    def getMin(self) -> int:
        if self.__is_empty():
            return -1
        return self.data[-1][1]

    def __is_empty(self) -> bool:
        return len(self.data) == 0
