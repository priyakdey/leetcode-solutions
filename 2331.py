"""
2331. Evaluate Boolean Binary Tree

You are given the root of a full binary tree with the following properties:

- Leaf nodes have either the value 0 or 1, where 0 represents False and 1 
  represents True.
- Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean 
  OR and 3 represents the boolean AND.

The evaluation of a node is as follows:

- If the node is a leaf node, the evaluation is the value of the node, i.e. 
  True or False.
- Otherwise, evaluate the node's two children and apply the boolean operation of 
  its value with the children's evaluations.

Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.
"""

from typing import Optional

from model import TreeNode


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            raise Exception("Invalid input")

        if root.left is None and root.right is None:
            return root.val == 1

        if (root.left is None and root.right is not None) or (
            root.left is not None and root.right is None
        ):
            raise Exception("Invalid input")

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
