"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) 
node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest 
node in T that has both p and q as descendants (where we allow a node to be a 
descendant of itself).”
"""

from model import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:

        smaller, greater = p, q
        if p.val > q.val:
            smaller, greater = q, p

        lca_node = root
        while lca_node != smaller and lca_node != greater:
            if smaller.val < lca_node.val and greater.val > lca_node.val:  # type: ignore
                break

            if smaller.val > lca_node.val and greater.val > lca_node.val:  # type: ignore
                lca_node = lca_node.right  # type: ignore
            if smaller.val < lca_node.val and greater.val < lca_node.val:  # type: ignore
                lca_node = lca_node.left  # type: ignore

        return lca_node  # type: ignore
