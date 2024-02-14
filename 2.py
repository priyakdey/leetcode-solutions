"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a 
single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.

"""

from typing import Optional

from model import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        return self.add_two_numbers(l1, l2, 0)

    def add_two_numbers(
        self, curr1: Optional[ListNode], curr2: Optional[ListNode], carry: int
    ) -> Optional[ListNode]:
        if curr1 is None and curr2 is None:
            return ListNode(1) if carry == 1 else None

        value: int = carry
        next_node1, next_node2 = None, None

        if curr1 is not None:
            next_node1 = curr1.next
            value += curr1.val

        if curr2 is not None:
            next_node2 = curr2.next
            value += curr2.val

        carry = value // 10
        value = value % 10
        node = ListNode(value)
        node.next = self.add_two_numbers(next_node1, next_node2, carry)
        return node
