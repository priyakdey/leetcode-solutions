"""
148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.
"""

from typing import Optional, cast

from model import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sort(node: Optional[ListNode]) -> ListNode:
            if node is None or node.next is None:
                return node  # type: ignore

            # find mid
            mid = findMid(node)
            left = node
            right = mid.next
            mid.next = None  # remove reference to merge it

            left = sort(left)
            right = sort(right)

            merged_head = merge(left, right)
            return merged_head

        def findMid(node: ListNode) -> ListNode:
            mid = node
            curr = node.next
            while curr is not None and curr.next is not None:
                mid = mid.next  # type: ignore
                curr = curr.next.next

            return mid  # type: ignore

        def merge(head1: ListNode, head2: ListNode):
            head = head1
            curr1, curr2 = head1.next, head2
            prev = head1

            if head2.val < head1.val:
                head = head2
                curr1, curr2 = head2.next, head1
                prev = head2

            while curr1 is not None and curr2 is not None:
                if curr1.val <= curr2.val:
                    prev = curr1
                    curr1 = curr1.next
                else:
                    _next = curr2.next
                    prev.next = curr2
                    prev = prev.next
                    curr2.next = curr1
                    curr2 = _next

            if curr2 is not None:
                prev.next = curr2

            return head

        if head is None or head.next is None:
            return head

        head = sort(head)
        return head
