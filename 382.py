"""
382. Linked List Random Node

Given a singly linked list, return a random node's value from the linked list. 
Each node must have the same probability of being chosen.

Implement the Solution class:

- Solution(ListNode head) Initializes the object with the head of the 
  singly-linked list head.
- int getRandom() Chooses a node randomly from the list and returns its value. 
  All the nodes of the list should be equally likely to be chosen.
"""

from random import randint
from typing import Optional, cast

from model import ListNode


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        random_node = self.head
        curr = self.head

        i = 1

        while curr is not None:
            if randint(1, i) == i:
                random_node = curr
            i += 1
            curr = curr.next

        return cast(ListNode, random_node).val
