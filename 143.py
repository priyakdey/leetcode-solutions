"""
143. Reorder List

You are given the head of a singly linked-list. 
The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. 
Only nodes themselves may be changed.
"""

from typing import Optional, cast

from model import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return

        mid = self.find_mid(head)
        head2 = mid.next
        mid.next = None

        head2 = self.reverse_list(cast(ListNode, head2))

        prev, curr1, curr2 = head, head.next, head2

        while curr1 is not None and curr2 is not None:
            next_node = curr2.next
            prev.next = curr2
            curr2.next = curr1
            prev = curr1
            curr1 = curr1.next
            curr2 = next_node

        if curr2 is not None:
            prev.next = curr2

    def reverse_list(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return cast(ListNode, prev)

    def find_mid(self, head: ListNode) -> ListNode:
        mid, curr = head, head.next
        while curr is not None and curr.next is not None:
            curr = curr.next.next
            mid = cast(ListNode, mid.next)

        return mid
