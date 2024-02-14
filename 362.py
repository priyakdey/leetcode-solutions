"""
362. Design Hit Counter

Design a hit counter which counts the number of hits received in the past 
5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and 
you may assume that calls are being made to the system in chronological order 
(i.e., timestamp is monotonically increasing). Several hits may arrive roughly 
at the same time.

Implement the HitCounter class:

- HitCounter() Initializes the object of the hit counter system.
- void hit(int timestamp) Records a hit that happened at timestamp (in seconds). 
  Several hits may happen at the same timestamp.
- int getHits(int timestamp) Returns the number of hits in the past 5 minutes 
  from timestamp (i.e., the past 300 seconds).
"""

from collections import deque
from typing import Deque


class HitCounter:
    def __init__(self):
        self.timestamps: Deque[int] = deque()

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        lower_bound = timestamp - 300 + 1
        left_index = self.index_of_gt_eq(lower_bound)
        if left_index == -1:
            return 0

        right_index = self.index_of_sm_eq(timestamp)
        if right_index == -1:
            return 0
        return right_index - left_index + 1

    def index_of_sm_eq(self, value: int) -> int:
        """Returns the index of the value or the index of the previous
        largest element element of value"""

        left, right = 0, len(self.timestamps) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if self.timestamps[mid] <= value:
                index = mid
                left = mid + 1
            else:
                right = mid - 1

        return index

    def index_of_gt_eq(self, value: int) -> int:
        """Returns the index of the value or index of next smallest
        element of value"""

        left, right = 0, len(self.timestamps) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if self.timestamps[mid] >= value:
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        return index
