"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in 
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

from heapq import heappop, heappush
from typing import List, Optional, Tuple

from model import ListNode


class ListNodeWrapper:

    def __init__(self, node: ListNode):
        self.node = node

    def __le__(self, other: ListNode):
        return self.node.val <= other.val

    def __lt__(self, other: Optional[ListNode]):
        return self.node.val < other.node.val  # type:ignore


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None:
            return None

        queue: List[ListNodeWrapper] = []

        for _list in lists:
            if _list is not None:
                heappush(queue, ListNodeWrapper(_list))

        if len(queue) == 0:
            return None

        head = heappop(queue).node
        curr = head

        if head.next is not None:
            heappush(queue, ListNodeWrapper(head.next))

        while len(queue) != 0:
            node = heappop(queue).node
            curr.next = node
            curr = curr.next
            if node.next is not None:
                heappush(queue, ListNodeWrapper(node.next))

        return head
