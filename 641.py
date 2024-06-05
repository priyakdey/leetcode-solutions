"""
641. Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

- MyCircularDeque(int k) Initializes the deque with a maximum size of k.
- boolean insertFront() Adds an item at the front of Deque. Returns true if the 
  operation is successful, or false otherwise.
- boolean insertLast() Adds an item at the rear of Deque. Returns true if the 
  operation is successful, or false otherwise.
- boolean deleteFront() Deletes an item from the front of Deque. Returns true 
  if the operation is successful, or false otherwise.
- boolean deleteLast() Deletes an item from the rear of Deque. Returns true if 
  the operation is successful, or false otherwise.
- int getFront() Returns the front item from the Deque. Returns -1 if the deque 
  is empty.
- int getRear() Returns the last item from Deque. Returns -1 if the deque 
  is empty.
- boolean isEmpty() Returns true if the deque is empty, or false otherwise.
- boolean isFull() Returns true if the deque is full, or false otherwise.
"""

from typing import List


class MyCircularDeque:

    def __init__(self, k: int):
        self.elements: List[int] = [0] * k
        self.capacity = k
        self.length = 0
        self.front = 0
        self.back = 0

    def insertFront(self, value: int) -> bool:
        if self.length == self.capacity:
            return False

        if self.length != 0:
            self.front = (self.front - 1) % self.capacity
        else:
            self.back = self.front

        self.elements[self.front] = value
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.length == self.capacity:
            return False

        if self.length != 0:
            self.back = (self.back + 1) % self.capacity
        else:
            self.front = self.back

        self.elements[self.back] = value
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if self.length == 0:
            return False

        if self.length != 0:
            self.front = (self.front + 1) % self.capacity

        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False

        if self.length != 0:
            self.back = (self.back - 1) % self.capacity

        self.length -= 1
        return True

    def getFront(self) -> int:
        if self.length == 0:
            return -1

        return self.elements[self.front]

    def getRear(self) -> int:
        if self.length == 0:
            return -1

        return self.elements[self.back]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity
