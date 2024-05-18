"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

from typing import Optional, cast

from model import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr, mid = head, head

        while curr is not None and curr.next is not None:
            mid = cast(ListNode, mid.next)
            curr = curr.next.next

        return mid
