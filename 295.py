"""
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value, and the median is 
the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data 
  structure.
- double findMedian() returns the median of all elements so far. 
  Answers within 10-5 of the actual answer will be accepted.
"""

from heapq import heappop, heappush
from typing import List


class MedianFinder:

    def __init__(self):
        self.left: List[int] = []
        self.right: List[int] = []
        self.median: float = 0.0

    def addNum(self, num: int) -> None:
        if num <= self.median:
            heappush(self.left, -num)
        else:
            heappush(self.right, num)

        self.balance()
        self.setMedian()

    def findMedian(self) -> float:
        return self.median

    def balance(self) -> None:
        if (
            len(self.left) == len(self.right)
            or abs(len(self.left) - len(self.right)) == 1
        ):
            return

        if len(self.left) > len(self.right):
            num = -heappop(self.left)
            heappush(self.right, num)
        else:
            num = heappop(self.right)
            heappush(self.left, -num)

    def setMedian(self) -> None:
        if len(self.left) > len(self.right):
            self.median = float(-self.left[0])
        elif len(self.left) < len(self.right):
            self.median = float(self.right[0])
        else:
            self.median = (-self.left[0] + self.right[0]) / 2
