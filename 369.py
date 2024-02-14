"""
369. Plus One Linked List

Given a non-negative integer represented as a linked list of digits, 
plus one to the integer.

The digits are stored such that the most significant digit is at the head of 
the list.
"""

from model import ListNode


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if head is None:
            raise Exception("invalid input")

        if head.next is None:
            val = head.val + 1
            carry = val // 10
            val = val % 10
            head.val = val
            if carry == 1:
                node = ListNode(1)
                node.next = head
                head = node
            return head

        head = self.reverse_list(head)
        tail = None
        curr = head
        carry = 1
        while curr is not None:
            val = curr.val + carry
            carry = val // 10
            val = val % 10
            curr.val = val
            tail = curr
            curr = curr.next

        if carry == 1:
            tail.next = ListNode(1)

        return self.reverse_list(head)

    def reverse_list(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
