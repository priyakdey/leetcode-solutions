from typing import Deque, List, Optional, Tuple


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        assert root is not None
        if root.left is None and root.right is None:
            return 1

        level_sum: List[int] = []
        queue: Deque[Tuple[TreeNode, int]] = deque()
        queue.append((root, 0))

        while len(queue) > 0:
            node, level = queue.popleft()

            if level >= len(level_sum):
                level_sum.append(node.val)
            else:
                level_sum[level] += node.val

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

        max_level = 0
        max_sum = level_sum[0]

        for level, total in enumerate(level_sum):
            if total > max_sum:
                max_sum = total
                max_level = level

        return max_level + 1
