"""
426. Convert Binary Search Tree to Sorted Doubly Linked List

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor 
and successor pointers in a doubly-linked list. 
For a circular doubly linked list, the predecessor of the first element is the 
last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, 
the left pointer of the tree node should point to its predecessor, 
and the right pointer should point to its successor. 
You should return the pointer to the smallest element of the linked list.
"""

from collections import deque
from typing import Optional, cast


class Node:
    """Definition for a Node."""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None:
            return root

        if root.left is None and root.right is None:
            root.left = root
            root.right = root
            return root

        stack = deque()
        curr = root
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        head: Optional[Node] = None
        prev: Optional[Node] = None

        while len(stack) != 0:
            curr = stack.pop()
            if head is None:
                head = curr

            if prev is not None:
                prev.right = curr
            curr.left = prev
            prev = curr

            child = curr.right
            while child is not None:
                stack.append(child)
                child = child.left

        tail: Node = cast(Node, head)
        while tail.right is not None:
            tail = tail.right

        tail.right = head
        cast(Node, head).left = tail
        return head
