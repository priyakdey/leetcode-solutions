"""
129. Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. 
Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""

from typing import Optional
from model import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode], number: int) -> int:
            nonlocal total

            if node.left is None and node.right is None:
                number = number * 10 + node.val
                total += number
                return

            number = number * 10 + node.val
            if node.left is not None:
                traverse(node.left, number)
            if node.right is not None:
                traverse(node.right, number)

            number = (number - node.val) // 10

        if root is None:
            raise Exception("invalid argument")

        if root.left is None and root.right is None:
            return root.val

        total = 0
        traverse(root, 0)
        return total
