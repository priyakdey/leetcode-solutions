"""
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.
"""

from typing import Optional, cast

from model import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        length = self.find_length(head)
        k = k % length

        if k != 0:
            head = self.reverse_list(head)

            curr = head

            while k > 1:
                curr = cast(ListNode, curr.next)
                k -= 1

            head2 = cast(ListNode, curr.next)
            curr.next = None

            head, head2 = self.reverse_list(head), self.reverse_list(head2)

            tail = head
            while tail.next is not None:
                tail = tail.next
            tail.next = head2

        return head

    def find_length(self, head: ListNode) -> int:
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next

        return length

    def reverse_list(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return cast(ListNode, prev)
