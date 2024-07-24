"""
863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an
integer k, return an array of the values of all nodes that have a distance k
from the target node.

You can return the answer in any order.
"""

from typing import List, Optional, Dict

from model import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node: TreeNode, k: int) -> None:
            nonlocal nodes

            if node is None:
                return
            if k == 0:
                nodes.append(node.val)

            if node.left is not None:
                dfs(node.left, k - 1)
            if node.right is not None:
                dfs(node.right, k - 1)

        def visit_parent(node: TreeNode, k: int) -> None:
            nonlocal parent_mapping

            if parent_mapping[node] is None:
                return

            parent = parent_mapping[node]
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            dfs(parent, k - 1)
            visit_parent(parent, k - 1)

        nodes: List[int] = []
        parent_mapping: Dict[TreeNode, Optional[TreeNode]] = {}
        self.generate_parent_mapping(root, None, parent_mapping)
        dfs(target, k)
        print(nodes)

        visit_parent(target, k)
        return nodes

    def generate_parent_mapping(
        self,
        node: TreeNode,
        parent: Optional[TreeNode],
        parent_mapping: Dict[TreeNode, Optional[TreeNode]],
    ) -> None:
        parent_mapping[node] = parent
        if node.left is not None:
            self.generate_parent_mapping(node.left, node, parent_mapping)
        if node.right is not None:
            self.generate_parent_mapping(node.right, node, parent_mapping)
