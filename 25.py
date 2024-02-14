"""
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, 
and return the modified list.

k is a positive integer and is less than or equal to the length of the 
linked list. If the number of nodes is not a multiple of k then left-out nodes, 
in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be 
changed.
"""

from typing import Optional

from model import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        if head is None or head.next is None:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = head

        self.traverse(dummy_head, head, None, 1, k)
        return dummy_head.next

    def traverse(
        self,
        attach_to: Optional[ListNode],
        curr: Optional[ListNode],
        group_head: Optional[ListNode],
        count: int,
        k: int,
    ) -> None:
        if curr is None:
            attach_to.next = group_head
            return

        if count == 1:
            group_head = curr

        if count < k:
            self.traverse(attach_to, curr.next, group_head, count + 1, k)
        if count == k:
            next_node = curr.next
            group_tail = curr
            group_tail.next = None
            group_tail = group_head
            group_head = self.reverse_list(group_head, None)
            attach_to.next = group_head
            attach_to = group_tail
            self.traverse(attach_to, next_node, None, 1, k)

    def reverse_list(
        self, curr: Optional[ListNode], prev: Optional[ListNode]
    ) -> Optional[ListNode]:
        if curr is None:
            return prev
        next_node = curr.next
        curr.next = prev
        return self.reverse_list(next_node, curr)
