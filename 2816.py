"""
2816. Double a Number Represented as a Linked List

You are given the head of a non-empty linked list representing a non-negative 
integer without leading zeroes.

Return the head of the linked list after doubling it.
"""

from typing import cast

from model import ListNode


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            raise Exception("invalid input. expecting a non empty list")

        head = self.reverse(head)
        tail, curr = None, head
        carry = 0

        while curr is not None:
            val = curr.val * 2 + carry
            carry = val // 10
            val = val % 10
            curr.val = val
            tail = curr
            curr = curr.next

        if carry != 0:
            tail.next = ListNode(carry)

        return self.reverse(head)

    def reverse(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return cast(ListNode, prev)
