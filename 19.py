"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list 
and return its head.
"""

from typing import Optional

from model import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            if n == 0:
                return None
            raise Exception("not enough nodes to delete")
        if head.next is None:
            if n == 1:
                return None
            raise Exception("not enough nodes to delete")

        tail = head
        while tail.next is not None and n > 0:
            tail = tail.next
            n -= 1

        if n != 0:
            raise Exception("not enough nodes to delete")

        prev = None
        curr = head
        while tail.next is not None:
            prev = curr
            curr = curr.next  # type: ignore
            tail = tail.next

        if prev is None:
            # remove the head
            head = head.next
        else:
            prev.next = curr.next  # type: ignore
            curr = None  # free(*node)

        return head
