"""
2674. Split a Circular Linked List

Given a circular linked list list of positive integers, your task is to split it 
into 2 circular linked lists so that the first one contains the first half of 
the nodes in list (exactly ceil(list.length / 2) nodes) in the same order they 
appeared in list, and the second one contains the rest of the nodes in list in 
the same order they appeared in list.

Return an array answer of length 2 in which the first element is a circular 
linked list representing the first half and the second element is a circular 
linked list representing the second half.

A circular linked list is a normal linked list with the only difference being 
that the last node's next node, is the first node.
"""

from typing import List, Optional, Set

from model import ListNode


class Solution:
    def splitCircularLinkedList(
        self, list: Optional[ListNode]
    ) -> List[Optional[ListNode]]:
        if list is None:
            return [None]

        tail = self.find_tail(list)
        tail.next = None
        mid = self.find_mid(list)
        head1 = list
        head2 = mid.next
        mid.next = head1
        tail.next = head2
        return [head1, head2]

    def find_mid(self, head: ListNode) -> ListNode:
        mid, curr = head, head.next
        while curr is not None and curr.next is not None:
            mid = mid.next
            curr = curr.next.next

        return mid

    def find_tail(self, head: ListNode) -> ListNode:
        visited: Set[ListNode] = set()
        tail: ListNode = head
        while tail.next not in visited:
            visited.add(tail)
            tail = tail.next

        return tail
