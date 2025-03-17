from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode(-1)
        even_head = ListNode(-1)

        index = 1
        curr = head
        curr1, curr2 = odd_head, even_head

        while curr is not None:
            if (index & 1) == 0:
                curr2.next = curr
                curr2 = curr2.next
            else:
                curr1.next = curr
                curr1 = curr1.next
            index += 1
            curr = curr.next

        curr1.next = even_head.next
        curr2.next = None
        return odd_head.next
