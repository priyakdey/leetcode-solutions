from typing import Dict, Optional, Tuple


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def get_max_loot(node: TreeNode, parent_looted: bool) -> int:
            nonlocal cache

            if node.left is None and node.right is None:
                return node.val if not parent_looted else 0

            key = (node, parent_looted)
            if key in cache:
                return cache[key]

            # case where we do not loot the current node
            max_loot_1 = 0
            if node.left is not None:
                max_loot_1 += get_max_loot(node.left, False)
            if node.right is not None:
                max_loot_1 += get_max_loot(node.right, False)

            # case where we loot the current node if possible
            max_loot_2 = 0
            if not parent_looted:
                max_loot_2 = node.val
                if node.left is not None:
                    max_loot_2 += get_max_loot(node.left, True)
                if node.right is not None:
                    max_loot_2 += get_max_loot(node.right, True)

            max_loot = max(max_loot_1, max_loot_2)
            cache[key] = max_loot
            return max_loot

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val

        cache: Dict[Tuple[TreeNode, bool]] = {}
        return max(get_max_loot(root, False), get_max_loot(root, True))
