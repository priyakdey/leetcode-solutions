"""
622. Design Circular Queue

Design your implementation of the circular queue. The circular queue is a 
linear data structure in which the operations are performed based on FIFO 
(First In First Out) principle, and the last position is connected back to the 
first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces 
in front of the queue. In a normal queue, once the queue becomes full, 
we cannot insert the next element even if there is a space in front of the queue. 
But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

- MyCircularQueue(k) Initializes the object with the size of the queue to be k.
- int Front() Gets the front item from the queue. If the queue is empty, 
  return -1.
- int Rear() Gets the last item from the queue. If the queue is empty, 
  return -1.
- boolean enQueue(int value) Inserts an element into the circular queue. 
  Return true if the operation is successful.
- boolean deQueue() Deletes an element from the circular queue. 
  Return true if the operation is successful.
- boolean isEmpty() Checks whether the circular queue is empty or not.
- boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in 
your programming language. 
"""

from typing import List


class MyCircularQueue:

    def __init__(self, k: int):
        self.buffer: List[int] = [0] * k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % len(self.buffer)
        self.buffer[self.rear] = value

        if self.front == -1:
            self.front = self.rear

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.buffer)

        return True

    def Front(self) -> int:
        return self.buffer[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.buffer[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.buffer) == self.front
