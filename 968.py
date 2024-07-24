"""
968. Binary Tree Cameras

You are given the root of a binary tree. We install cameras on the tree nodes
where each camera at a node can monitor its parent, itself, and its immediate
children.

Return the minimum number of cameras needed to monitor all nodes of the tree.
"""

from typing import Optional

from model import TreeNode


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal camera, NOT_NEEDED, HAS_CAMERA, NEED_CAMERA

            if node is None:
                return NOT_NEEDED

            left_camera = dfs(node.left)
            right_camera = dfs(node.right)

            if left_camera == NEED_CAMERA or right_camera == NEED_CAMERA:
                camera += 1
                return HAS_CAMERA

            if left_camera == HAS_CAMERA or right_camera == HAS_CAMERA:
                return NOT_NEEDED

            return NEED_CAMERA

        NOT_NEEDED = 0
        HAS_CAMERA = 1
        NEED_CAMERA = 2

        camera = 0

        if root is None:
            raise Exception("invalid arguments")

        if root.left is None and root.right is None:
            return 1

        if dfs(root) == NEED_CAMERA:
            camera += 1

        return camera
