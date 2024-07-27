"""
1740. Find Distance in a Binary Tree

Given the root of a binary tree and two integers p and q, return the distance
between the nodes of value p and value q in the tree.

The distance between two nodes is the number of edges on the path from one to
the other.
"""

from typing import Optional, Dict, Set

from model import TreeNode


class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if root is None:
            raise Exception("invalid arguments")
        if root is None or p == q:
            return 0

        mapping: Dict[int, int] = {}
        Solution.node_parent_mapping(root, None, mapping)

        if p not in mapping or q not in mapping:
            raise Exception("invalid arguments")

        visited: Set[int] = set()
        distance: int = 0
        distance_map: Dict[int, int] = {}

        while p in mapping:
            if p == q:
                return distance

            visited.add(p)
            distance_map[p] = distance
            distance += 1
            p = mapping[p]

        distance = 0
        while q not in visited:
            q = mapping[q]
            distance += 1

        return distance + distance_map[q]

    @staticmethod
    def node_parent_mapping(
        node: TreeNode, parent: Optional[TreeNode], mapping: Dict[int, int]
    ):
        mapping[node.val] = parent.val if parent is not None else -1

        if node.left is not None:
            Solution.node_parent_mapping(node.left, node, mapping)
        if node.right is not None:
            Solution.node_parent_mapping(node.right, node, mapping)
