"""
3294. Convert Doubly Linked List to Array II

You are given an arbitrary node from a doubly linked list, which contains
nodes that have a next pointer and a previous pointer.

Return an integer array which contains the elements of the linked list in order.
"""

from typing import List, Optional


class Node:
    """Definition for a Node."""

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def toArray(self, node: "Optional[Node]") -> List[int]:
        if node is None:
            return []
        if node.next is None and node.prev is None:
            return [node.val]

        nodes: List[int] = [node.val]
        next_node = node.next
        while next_node is not None:
            nodes.append(next_node.val)
            next_node = next_node.next

        prev_node = node.prev
        while prev_node is not None:
            nodes.insert(0, prev_node.val)
            prev_node = prev_node.prev

        return nodes
