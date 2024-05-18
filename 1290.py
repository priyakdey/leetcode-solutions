"""
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
"""

from typing import cast

from model import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            raise Exception("invalid input")

        _head = self.reverse_list(head)

        curr = _head
        value = 0
        bit_position = 0

        while curr is not None:
            value += (1 << bit_position) * curr.val
            bit_position += 1
            curr = curr.next

        return value

    def reverse_list(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return cast(ListNode, prev)
