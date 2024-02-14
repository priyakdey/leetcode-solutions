"""
817. Linked List Components

You are given the head of a linked list containing unique integer values and an 
integer array nums that is a subset of the linked list values.

Return the number of connected components in nums where two values are connected 
if they appear consecutively in the linked list.
"""

from typing import List, Optional

from model import ListNode


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        unique_nums = set(nums)

        curr = head
        connected_component_count = 0

        while curr is not None:
            if curr.val in unique_nums:
                connected_component_count += 1
                while curr is not None and curr.val in unique_nums:
                    curr = curr.next
                continue
            curr = curr.next

        return connected_component_count
