"""
281. Zigzag Iterator

Given two vectors of integers v1 and v2, implement an iterator to return their 
elements alternately.

Implement the ZigzagIterator class:
- ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the 
  two vectors v1 and v2.
- boolean hasNext() returns true if the iterator still has elements, and 
  false otherwise.
- int next() returns the current element of the iterator and moves the iterator 
  to the next element.
"""

from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.curr1 = 0
        self.curr2 = 0
        self.vec_inc = True
        self.length = len(v1) + len(v2)

    def next(self) -> int:
        if self.curr1 == len(self.v1):
            element = self.v2[self.curr2]
            self.curr2 += 1
        elif self.curr2 == len(self.v2):
            element = self.v1[self.curr1]
            self.curr1 += 1
        elif self.vec_inc:
            element = self.v1[self.curr1]
            self.curr1 += 1
            self.vec_inc = False
        else:
            element = self.v2[self.curr2]
            self.curr2 += 1
            self.vec_inc = True

        self.length -= 1
        return element

    def hasNext(self) -> bool:
        return self.length > 0


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
