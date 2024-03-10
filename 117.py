"""
117. Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next 
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""

from typing import List


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,  # type: ignore
        right: "Node" = None,  # type: ignore
        next: "Node" = None,  # type: ignore
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if root is None or root.left is None and root.right is None:
            return root

        curr_level: List[Node] = [root]
        next_level: List[Node] = []

        while len(curr_level) != 0:
            node = curr_level.pop(0)

            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)

            if len(curr_level) == 0 and len(next_level) != 0:
                for i in range(len(next_level) - 1):
                    next_level[i].next = next_level[i + 1]
                curr_level = next_level
                next_level = []

        return root
