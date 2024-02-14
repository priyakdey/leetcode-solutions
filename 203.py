"""
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the 
linked list that has Node.val == val, and return the new head.
"""

from typing import Optional

from model import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head

        prev = dummy_head
        curr = head
        prev = self.remove_node_with_val(curr, prev, val)
        prev.next = None
        return dummy_head.next

    def remove_node_with_val(
        self, curr: Optional[ListNode], prev: ListNode, val: int
    ) -> ListNode:
        if curr is None:
            return prev

        if curr.val != val:
            prev.next = curr
            prev = prev.next

        return self.remove_node_with_val(curr.next, prev, val)
