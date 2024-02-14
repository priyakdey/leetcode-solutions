"""
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

"""

from collections import deque
from typing import Deque, Optional, Tuple


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None or (root.left is None and root.right is None):
            return root

        queue: Deque[Tuple[Node, int]] = deque()
        queue.append((root, 0))

        while len(queue) != 0:
            node, level = queue.popleft()

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

            if len(queue) != 0 and queue[0][1] == level:
                node.next = queue[0][0]

        return root


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Optional[Node]" = None,
        right: "Optional[Node]" = None,
        next: "Optional[Node]" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
