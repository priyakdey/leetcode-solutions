"""
380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present.
  Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present.
  Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements
  (it's guaranteed that at least one element exists when this method is called).
  Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in
average O(1) time complexity.
"""

import random
from typing import Dict, List


class RandomizedSet:

    def __init__(self):
        self.elements: List[int] = []
        self.value_index_map: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.value_index_map:
            return False

        self.elements.append(val)
        self.value_index_map[val] = len(self.elements) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_index_map:
            return False

        index = self.value_index_map[val]
        last_element = self.elements[-1]
        self.elements[index] = last_element
        self.value_index_map[last_element] = index
        self.elements.pop()
        del self.value_index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)
