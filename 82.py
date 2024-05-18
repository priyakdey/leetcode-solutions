"""
82. Remove Duplicates from Sorted List II


Given the head of a sorted linked list, delete all nodes that have duplicate 
numbers, leaving only distinct numbers from the original list. 
Return the linked list sorted as well.
"""

from typing import Optional

from model import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy_head = ListNode()  # dummy.next points to the head
        dummy_curr = dummy_head

        curr = head
        while curr is not None:
            if curr.next is not None and curr.val == curr.next.val:
                while curr.next is not None and curr.val == curr.next.val:
                    # skip all the nodes with same value
                    curr = curr.next
            else:
                # curr node has unique val
                dummy_curr.next = curr
                dummy_curr = dummy_curr.next
            curr = curr.next

        # remove last nodes if any
        dummy_curr.next = None
        return dummy_head.next
