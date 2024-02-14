"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing 
together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional

from model import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return list1
        if list1 is None or list2 is None:
            return list1 if list2 is None else list2

        head = list1
        prev = list1
        curr1 = list1.next
        curr2 = list2

        if list2.val < list1.val:
            head = list2
            prev = list2
            curr1 = list2.next
            curr2 = list1

        self.merge(curr1, curr2, prev)

        return head

    def merge(
        self, curr1: Optional[ListNode], curr2: Optional[ListNode], prev: ListNode
    ) -> None:
        """Merges two lists.

        :param: curr1 pointer to current node in list1
        :param: curr2 pointer to current node in list2
        :param: prev pointer to previous node in list1
        """
        if curr1 is None and curr2 is None:
            return

        if curr1 is None:
            prev.next = curr2
            return

        if curr2 is None:
            return

        if curr1.val <= curr2.val:
            curr1 = curr1.next
        else:
            next_node = curr2.next
            prev.next = curr2
            curr2.next = curr1
            curr2 = next_node

        prev = prev.next
        self.merge(curr1, curr2, prev)
