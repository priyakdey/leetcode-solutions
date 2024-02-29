"""
160. Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
"""

from typing import Optional

from model import ListNode


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if headA is None and headB is None:
            return None
        if headA is not None and headB is None:
            return headA
        if headA is None and headB is not None:
            return headB

        def getSize(node: ListNode) -> int:
            size = 0
            while node is not None:
                size += 1
                node = node.next  # type: ignore

            return size

        def n_node_from_head(node: ListNode, n: int) -> ListNode:
            while node is not None and n > 0:
                node = node.next  # type: ignore
                n -= 1

            return node

        # find length of two lists
        len1, len2 = getSize(headA), getSize(headB)
        n = abs(len1 - len2)
        curr1, curr2 = headA, n_node_from_head(headB, n)
        if len1 > len2:
            # if len2 is bigger, we need to offset list B
            curr1, curr2 = n_node_from_head(headA, n), headB

        intersection_node = None

        # now iterate over the two list to find intersection
        while curr1 is not None and curr2 is not None:
            if curr1 == curr2:
                intersection_node = curr1
                break
            curr1 = curr1.next
            curr2 = curr2.next

        return intersection_node
