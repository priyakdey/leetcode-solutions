"""
328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices 
together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain 
as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

from typing import Optional

from model import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head

        odd_head, even_head = ListNode(-1), ListNode(-1)
        odd_curr, even_curr = odd_head, even_head
        curr = head

        i = 1

        while curr is not None:
            if i & 1 == 0:
                even_curr.next = curr
                even_curr = even_curr.next
            else:
                odd_curr.next = curr
                odd_curr = odd_curr.next
            curr = curr.next
            i += 1

        odd_curr.next = even_head.next
        even_curr.next = None
        return odd_head.next
