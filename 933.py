from collections import deque
from typing import Deque


class RecentCounter:

    def __init__(self):
        self.pings: Deque[int] = deque()

    def ping(self, t: int) -> int:
        while len(self.pings) > 0 and self.pings[0] < t - 3000:
            self.pings.popleft()

        self.pings.append(t)
        return len(self.pings)
