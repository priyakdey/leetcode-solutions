from collections import defaultdict
from typing import Dict, List, Tuple


class TimeMap:

    def __init__(self):
        self.table: Dict[str, List[Tuple[str, int]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            """"""

        values: List[Tuple[str, int]] = self.table[key]
        left, right = 0, len(values) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][1] <= timestamp:
                index = mid
                left = mid + 1
            else:
                right = mid - 1

        return values[index][0] if index != -1 else ""
