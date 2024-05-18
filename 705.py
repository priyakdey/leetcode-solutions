"""
706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

- MyHashMap() initializes the object with an empty map.
- void put(int key, int value) inserts a (key, value) pair into the HashMap. 
  If the key already exists in the map, update the corresponding value.
- int get(int key) returns the value to which the specified key is mapped, 
  or -1 if this map contains no mapping for the key.
- void remove(key) removes the key and its corresponding value if the map 
  contains the mapping for the key.
"""

from typing import Dict, List, Optional, Tuple, cast


class Node:
    """Represents a node in the singly linked list."""

    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.next: Optional[Node] = None


class MyHashMap:

    def __init__(self):
        self.table: List[Optional[Node]] = [None for _ in range(1 << 4)]

    def put(self, key: int, value: int) -> None:
        index = hash(key) % len(self.table)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            return

        curr = cast(Node, self.table[index])
        tail = curr

        while curr is not None:
            if curr.key == key:
                break
            tail = curr
            curr = curr.next

        if curr is not None:
            curr.value = value
        else:
            tail.next = Node(key, value)

    def get(self, key: int) -> int:
        index = hash(key) % len(self.table)

        if self.table[index] is None:
            return -1

        value = -1
        curr = cast(Node, self.table[index])
        while curr is not None:
            if curr.key == key:
                value = curr.value
                break
            curr = curr.next

        return value

    def remove(self, key: int) -> None:
        index = hash(key) % len(self.table)

        if self.table[index] is None:
            return

        head = cast(Node, self.table[index])
        if head.key == key:
            self.table[index] = head.next
            return

        prev, curr = head, head.next

        while curr is not None:
            if curr.key == key:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
