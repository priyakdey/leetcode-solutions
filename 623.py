"""
623. Add One Row to Tree

Given the root of a binary tree and two integers val and depth, add a row of 
nodes with value val at the given depth depth.

Note that the root node is at depth 1.


The adding rule is:
- Given the integer depth, for each not null tree node cur at the depth 
  depth - 1, create two tree nodes with value val as cur's left subtree root 
  and right subtree root.
- cur's original left subtree should be the left subtree of the new left 
  subtree root.  
- cur's original right subtree should be the right subtree of the new right 
  subtree root.
- If depth == 1 that means there is no depth depth - 1 at all, then create a 
  tree node with value val as the new root of the whole original tree, and the 
  original tree is the new root's left subtree.
"""

from model import TreeNode


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            root = node
            return root

        self.insert_node(root, val, depth - 1)
        return root

    def insert_node(self, node: Optional[TreeNode], val: int, depth: int) -> None:
        if node is None:
            return

        if depth == 1:
            left, right = node.left, node.right

            node.left = TreeNode(val)
            node.right = TreeNode(val)

            node.left.left = left
            node.right.right = right
            return

        self.insert_node(node.left, val, depth - 1)
        self.insert_node(node.right, val, depth - 1)
