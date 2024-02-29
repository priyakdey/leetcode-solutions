"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the 
reversed list.

"""

from typing import Optional

from model import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse_list(head, None)

    def reverse_list(
        self, curr: Optional[ListNode], prev: Optional[ListNode]
    ) -> Optional[ListNode]:
        if curr is None:
            return prev
        next_node = curr.next
        curr.next = prev
        return self.reverse_list(next_node, curr)
