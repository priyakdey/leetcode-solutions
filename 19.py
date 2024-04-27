"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list 
and return its head.
"""

from typing import Optional, Tuple, cast

from model import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head: ListNode = ListNode(-1)
        dummy_head.next = head

        prev_node, found = self.find_nth_node_from_end(dummy_head, n)

        if not found:
            raise Exception("not enough node")

        prev_node = cast(ListNode, prev_node)
        prev_node.next = prev_node.next.next  # type: ignore

        return dummy_head.next

    def find_nth_node_from_end(
        self, head: ListNode, n: int
    ) -> Tuple[Optional[ListNode], bool]:
        """Returns the nth node from the end. If no such node found returns the
        second value as false
        """
        tail = head

        while tail is not None and n > 0:
            tail = tail.next
            n -= 1

        if tail is None:
            return None, False

        node = head
        while tail.next is not None:
            node = cast(ListNode, node.next)
            tail = tail.next

        return node, True
