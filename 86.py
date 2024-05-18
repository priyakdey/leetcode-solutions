"""
86. Partition List

Given the head of a linked list and a value x, partition it such that all nodes 
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of 
the two partitions.
"""

from typing import Optional

from model import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy_head1, dummy_head2 = ListNode(-1), ListNode(-1)
        curr1, curr2 = dummy_head1, dummy_head2

        curr = head

        while curr is not None:
            if curr.val < x:
                curr1.next = curr
                curr1 = curr1.next
            else:
                curr2.next = curr
                curr2 = curr2.next
            curr = curr.next

        curr1.next = dummy_head2.next
        curr2.next = None

        return dummy_head1.next
