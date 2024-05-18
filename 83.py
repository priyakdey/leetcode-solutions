"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each 
element appears only once. Return the linked list sorted as well.
"""

from typing import Optional

from model import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        insert_at, curr = head, head.next
        last_uniq_value = head.val

        while curr is not None:
            if curr.val != last_uniq_value:
                insert_at.next = curr
                insert_at = insert_at.next
                last_uniq_value = curr.val
            curr = curr.next

        insert_at.next = None
        return head
