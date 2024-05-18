"""
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where 
left <= right, reverse the nodes of the list from position left to position 
right, and return the reversed list.
"""

from typing import Optional

from model import ListNode


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head

        # 1.check length
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next

        if left == 1 and right >= length:
            # reverse the whole array
            prev = None
            curr = head

            while curr is not None:
                _next = curr.next
                curr.next = prev
                prev = curr
                curr = _next

            return prev

        # we need to first get the left - 1 node
        prev_node, left_node = None, head
        if left != 1:
            i = 1
            while i < left:
                prev_node = left_node
                left_node = left_node.next  # type: ignore
                i += 1

        # we need to that the right_node and preserve next node to right
        right_node, next_node = head, head.next  # type: ignore
        i = 1
        while i < right and right_node is not None:
            right_node = right_node.next
            next_node = right_node.next  # type: ignore
            i += 1

        # reverse from left_node to right_node
        right_node.next = None  # type: ignore
        curr = left_node
        prev = None
        while curr is not None:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        # connect prev_node to this new head
        if prev_node is not None:
            prev_node.next = prev
        else:
            head = prev

        # get the last node and connect to the next node
        curr = prev
        while curr.next is not None:  # type: ignore
            curr = curr.next  # type: ignore

        curr.next = next_node  # type: ignore

        return head
