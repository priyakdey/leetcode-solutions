"""
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the
given key in the BST. Return the root node reference (possibly updated) of
the BST.

Basically, the deletion can be divided into two stages:
- Search for a node to remove.
- If the node is found, delete the node.
"""

from typing import Optional, Tuple

from model import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            if root.val == key:
                return None
            else:
                return root

        node, parent = self.find_node(root, key)
        if node is None:
            return root
        if node is root:
            return self.remove_root(root)
        else:
            self.remove_node(node)
            return root

    def remove_root(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # TODO
        pass

    @staticmethod
    def find_node(
        root: TreeNode, key: int
    ) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
        parent, curr = None, root
        while curr is not None:
            if curr.val == key:
                break
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return curr, parent
