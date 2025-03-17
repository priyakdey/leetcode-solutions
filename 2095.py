from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        prev = None
        mid = head
        curr = head
        while curr is not None and curr.next is not None:
            prev = mid
            mid = mid.next
            curr = curr.next.next

        prev.next = mid.next
        return head
