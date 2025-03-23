import heapq
from typing import List


class SmallestInfiniteSet:

    def __init__(self):
        self.distinct: Set[int] = {num for num in range(1, 1001)}
        self.heap: List[int] = [num for num in range(1, 1001)]

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.heap)
        self.distinct.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.distinct:
            return

        self.distinct.add(num)
        heapq.heappush(self.heap, num)
