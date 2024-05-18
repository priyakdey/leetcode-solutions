"""
3063. Linked List Frequency

Given the head of a linked list containing k distinct elements, return the head 
to a linked list of length k containing the frequency of each distinct element 
in the given linked list in any order.
"""

from typing import Dict, Optional

from model import ListNode


class Solution:
    def frequenciesOfElements(
        self, dummy_head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if dummy_head is None:
            return None
        if dummy_head.next is None:
            return ListNode(1)

        freq_map: Dict[int, int] = {}
        curr = dummy_head
        while curr is not None:
            if curr.val not in freq_map:
                freq_map[curr.val] = 1
            else:
                freq_map[curr.val] += 1
            curr = curr.next

        dummy_head = ListNode(-1)
        curr = dummy_head

        for _, freq in freq_map.items():
            curr.next = ListNode(freq)
            curr = curr.next

        return dummy_head.next
