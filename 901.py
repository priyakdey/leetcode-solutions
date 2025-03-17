from collections import deque
from typing import Deque


class StockSpanner:

    def __init__(self):
        self.stack: Deque[Tuple[int, int]] = deque()

    def next(self, price: int) -> int:
        span = 1
        while len(self.stack) > 0 and stack[-1][0] <= price:
            _, _span = self.stack.pop()
            span += _span
        self.stack.append((price, span))
        return span
