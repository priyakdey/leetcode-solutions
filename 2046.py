"""
2046. Sort Linked List Already Sorted Using Absolute Values

Given the head of a singly linked list that is sorted in non-decreasing order 
using the absolute values of its nodes, return the list sorted in non-decreasing 
order using the actual values of its nodes.
"""

from typing import Optional

from model import ListNode


class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr, prev = head.next, head

        while curr is not None:
            if curr.val <= head.val:
                prev.next = curr.next
                curr.next = head
                head = curr
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return head
