"""
1836. Remove Duplicates From an Unsorted Linked List

Given the head of a linked list, find all the values that appear more than 
once in the list and delete the nodes that have any of those values.

Return the linked list after the deletions.
"""

from typing import Dict

from model import ListNode


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        freq_count: Dict[int, int] = {}
        curr = head
        while curr is not None:
            if curr.val in freq_count:
                freq_count[curr.val] += 1
            else:
                freq_count[curr.val] = 1

            curr = curr.next

        dummy_head = ListNode(-1)
        dummy_head.next = head
        attach_to = dummy_head
        curr = head

        while curr is not None:
            if freq_count[curr.val] == 1:
                attach_to.next = curr
                attach_to = attach_to.next
            curr = curr.next

        attach_to.next = None
        return dummy_head.next
