"""
1429. First Unique Number

You have a queue of integers, you need to retrieve the first unique integer
in the queue.

Implement the FirstUnique class:
- FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
- int showFirstUnique() returns the value of the first unique integer of the
  queue, and returns -1 if there is no such integer.
- void add(int value) insert value to the queue.
"""

from typing import Dict, List, Optional


class Node:

    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class LinkedList:

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def add(self, value: int) -> Node:
        node = Node(value)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1
        return node

    def remove(self, node: Node) -> None:
        if node is None:
            return

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            prev_node, next_node = node.prev, node.next
            if next_node is None:
                self.tail = node
                self.tail.next = None
                node.prev = None
            else:
                next_node.prev = prev_node
                prev_node.next = next_node

        self.size -= 1

    def get_head(self) -> Optional[Node]:
        return self.head


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.list = LinkedList()
        self.mapping: Dict[int, Node] = {}

        for num in nums:
            if num not in self.mapping:
                node = self.list.add(num)
                self.mapping[num] = node
            else:
                self.list.remove(self.mapping[num])

    def showFirstUnique(self) -> int:
        node = self.list.get_head()
        return node.value if node is not None else -1

    def add(self, value: int) -> None:
        if value in self.mapping:
            self.list.remove(self.mapping[value])
        else:
            self.mapping[value] = self.list.add(value)
