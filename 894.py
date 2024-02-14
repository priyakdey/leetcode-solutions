"""
894. All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. 
Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. 
You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
"""

from typing import List, Optional

from model import TreeNode


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(0)]

        trees: List[Optional[TreeNode]] = []
        root = TreeNode(0)
        self.generate_trees(1, n, root, root, trees)
        return trees

    def generate_trees(
        self,
        curr_node_count: int,
        total_nodes: int,
        root: TreeNode,
        curr: TreeNode,
        trees: List[Optional[TreeNode]],
    ) -> None:
        if curr_node_count == total_nodes:
            trees.append(self.deep_copy(root))
            return

        if total_nodes - curr_node_count < 2:
            return

        curr.left = TreeNode(0)
        curr.right = TreeNode(0)
        self.generate_trees(curr_node_count + 2, total_nodes, root, curr.left, trees)
        self.generate_trees(curr_node_count + 2, total_nodes, root, curr.right, trees)

    def deep_copy(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node is None:
            return None
        copy_node = TreeNode(node.val)
        copy_node.left = self.deep_copy(node.left)
        copy_node.right = self.deep_copy(node.right)
        return copy_node
