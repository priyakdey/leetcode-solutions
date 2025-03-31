INT_MIN = -(1 << 31)


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node: TreeNode, max_value: int) -> int:
            count = 0
            if node.val >= max_value:
                count += 1

            if node.left is None and node.right is None:
                return count

            if node.left is not None:
                count += traverse(node.left, max(node.val, max_value))
            if node.right is not None:
                count += traverse(node.right, max(node.val, max_value))

            return count

        return traverse(root, INT_MIN)
