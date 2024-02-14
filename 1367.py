"""
1367. Linked List in Binary Tree

Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head 
correspond to some downward path connected in the binary tree otherwise 
return False.

In this context downward path means a path that starts at some node and goes 
downwards.
"""

from typing import Optional
from model import ListNode, TreeNode


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if head is None and root is None:
            return True
        if head is None or root is None:
            return False

        return (
            self.matchFromNode(head, root)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )

    def matchFromNode(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if head is None:
            return True
        if root is None:
            return False

        return head.val == root.val and (
            self.matchFromNode(head.next, root.left)
            or self.matchFromNode(head.next, root.right)
        )
