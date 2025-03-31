from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def capture_leaf(node: TreeNode, leaves: List[int]) -> None:
            if node.left is None and node.right is None:
                leaves.append(node.val)
                return

            if node.left is not None:
                capture_leaf(node.left, leaves)
            if node.right is not None:
                capture_leaf(node.right, leaves)

        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        leaves1, leaves2 = [], []
        capture_leaf(root1, leaves1)
        capture_leaf(root2, leaves2)
        return leaves1 == leaves2
