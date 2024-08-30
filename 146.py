"""
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used 
(LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise 
  return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
  the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""

from typing import Dict, Optional


class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

    def __str__(self) -> str:
        return f"{self.key}:{self.value}"


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.kvs: Dict[int, Node] = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.kvs:
            return -1

        node = self.kvs[key]
        self.__make_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.kvs:
            node = self.kvs[key]
            node.value = value
            self.__make_head(node)
            return

        if self.size == self.capacity:
            self.__evict()

        node = Node(key, value)
        self.kvs[key] = node
        self.__append_node(node)

    def __append_node(self, node: Node) -> None:
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head

        node.next = next_node
        next_node.prev = node  # type: ignore

        self.size += 1

    def __evict(self) -> None:
        node = self.tail.prev
        node.prev.next = self.tail  # type: ignore
        self.tail.prev = node.prev  # type: ignore
        del self.kvs[node.key]  # type: ignore
        self.size -= 1

    def __make_head(self, node: Node) -> None:
        if node is self.head.next:
            return

        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node  # type: ignore
        next_node.prev = prev_node  # type: ignore

        next_node = self.head.next
        self.head.next = node
        node.prev = self.head

        node.next = next_node
        next_node.prev = node  # type: ignore

    def __str__(self) -> str:
        buffer = []
        curr = self.head
        while curr is not None:
            buffer.append(str(curr))
            curr = curr.next

        return f'table = {self.kvs} | nodes = {" <-> ".join(buffer)} | size = {self.capacity}'
