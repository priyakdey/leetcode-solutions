"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the 
preorder traversal of a binary tree and inorder is the inorder traversal of the 
same tree, construct and return the binary tree.
"""

from typing import List, Optional

from model import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        val = preorder[0]
        node = TreeNode(val)
        index = -1
        for i in range(0, len(inorder)):
            if inorder[i] == val:
                index = i
                break

        node.left = self.buildTree(preorder[1 : 1 + index], inorder[:index])
        node.right = self.buildTree(preorder[1 + index :], inorder[index + 1 :])
        return node
