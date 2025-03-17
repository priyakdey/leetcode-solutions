from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root

        while curr is not None:
            if curr.val == val:
                break
            elif curr.val < val:
                curr = curr.right
            else:
                curr = curr.left

        return curr
