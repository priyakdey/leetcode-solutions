"""
142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be 
reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer 
is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not 
passed as a parameter.

Do not modify the linked list.
"""

from typing import Optional

from model import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first detect if cycle does exists - tortoise hare race (Flyods cycle detection)
        slow_ptr, fast_ptr = head, head

        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next  # type: ignore
            fast_ptr = fast_ptr.next.next
            if fast_ptr == slow_ptr:
                break

        if fast_ptr is None or fast_ptr.next is None:
            # no cycle detected
            return None

        # move the fast pointer to the head and shift pointers by 1 node till they meet
        fast_ptr = head
        while fast_ptr != slow_ptr:
            slow_ptr = slow_ptr.next  # type: ignore
            fast_ptr = fast_ptr.next  # type: ignore

        return fast_ptr
