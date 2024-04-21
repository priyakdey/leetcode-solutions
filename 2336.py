"""
2336. Smallest Number in Infinite Set

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:
- SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain 
  all positive integers.
- int popSmallest() Removes and returns the smallest integer contained in the 
  infinite set.
- void addBack(int num) Adds a positive integer num back into the infinite set, 
  if it is not already in the infinite set.
"""

from heapq import heappop, heappush
from typing import List, Set


# TODO: Complete this


class SmallestInfiniteSet:

    def __init__(self):
        self.distinct: Set[int] = set()
        self.data: List[int] = []

    def popSmallest(self) -> int:
        smallest = heappop(self.data)
        self.distinct.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.distinct:
            return

        heappush(self.data, num)
        self.distinct.add(num)
