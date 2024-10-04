"""
3217. Delete Nodes From Linked List Present in Array

You are given an array of integers nums and the head of a linked list.
Return the head of the modified linked list after removing all nodes from
the linked list that have a value that exists in nums.
"""

from typing import List, Optional

from model import ListNode


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head: ListNode = ListNode(-1)
        dummy_head.next = head

        distinct = set(nums)

        prev, curr = dummy_head, head

        while curr is not None:
            if curr.val not in distinct:
                prev.next = curr
                prev = prev.next
            curr = curr.next

        prev.next = None
        return dummy_head.next
