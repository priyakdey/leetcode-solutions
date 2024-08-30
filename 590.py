"""
590. N-ary Tree Postorder Traversal

Given the root of an n-ary tree, return the postorder traversal of its nodes'
values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples)
"""

from typing import List


class Node:
    """Definition for a Node."""

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        def traverse(node: Node) -> None:
            nonlocal nodes

            if node is None:
                return

            if node.children is not None:
                for child in node.children:
                    traverse(child)

            nodes.append(node.val)

        nodes: List[int] = []
        traverse(root)
        return nodes
