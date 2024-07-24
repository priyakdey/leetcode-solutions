"""
285. Inorder Successor in BST

Given the root of a binary search tree and a node p in it, return the
in-order successor of that node in the BST. If the given node has no in-order
successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.
"""

from collections import deque
from typing import Optional, Deque

# from model import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        stack: Deque[TreeNode] = deque()

        if p.right is not None:
            successor = p.right
            while successor.left is not None:
                successor = successor.left

            return successor

        curr = root
        while curr != p:
            stack.append(curr)
            if p.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        while len(stack) != 0 and stack[-1].left != curr:
            curr = stack.pop()

        return stack[-1] if len(stack) != 0 else None
