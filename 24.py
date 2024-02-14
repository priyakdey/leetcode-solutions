"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)
"""

from typing import Optional

from model import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        return self.swap_pair(head.next, head)

    def swap_pair(
        self, curr: Optional[ListNode], prev: Optional[ListNode]
    ) -> Optional[ListNode]:
        if curr is None:
            return prev

        next_node = curr.next
        curr.next = prev
        prev.next = None

        if next_node is None:
            prev.next = None
        else:
            prev.next = self.swap_pair(next_node.next, next_node)

        return curr
