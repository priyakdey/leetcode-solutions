from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def find_mid(head: ListNode) -> ListNode:
            mid, curr = head, head.next
            while curr is not None and curr.next is not None:
                curr = curr.next.next
                mid = mid.next

            return mid

        def reverse(head: ListNode) -> ListNode:
            prev, curr = None, head

            while curr is not None:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev

        mid = find_mid(head)
        head2 = mid.next
        mid.next = None

        head2 = reverse(head2)

        max_value = -(1 << 31)
        curr1, curr2 = head, head2

        while curr1 is not None:
            max_value = max(max_value, curr1.val + curr2.val)
            curr1 = curr1.next
            curr2 = curr2.next

        return max_value
