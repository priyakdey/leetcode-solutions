"""
981. Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple values for 
the same key at different time stamps and retrieve the key's value at a 
certain timestamp.

Implement the TimeMap class:

- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with the 
  value value at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called 
  previously, with timestamp_prev <= timestamp. If there are multiple such values, 
  it returns the value associated with the largest timestamp_prev. 
  If there are no values, it returns "".
"""

from typing import Dict, List, Tuple


class TimeMap:

    def __init__(self):
        self.table: Dict[str, List[Tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = []

        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""

        index = self.find_index(key, timestamp)

        if index == -1:
            return ""

        return self.table[key][index][1]

    def find_index(self, key: str, timestamp: int) -> int:
        values = self.table[key]
        index = -1
        left, right = 0, len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                index = mid
                left = mid + 1
            else:
                right = mid - 1

        return index
