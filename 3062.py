"""
3062. Winner of the Linked List Game

You are given the head of a linked list of even length containing integers.

Each odd-indexed node contains an odd integer and each even-indexed node contains 
an even integer.

We call each even-indexed node and its next node a pair, e.g., the nodes with 
indices 0 and 1 are a pair, the nodes with indices 2 and 3 are a pair, and so on.

For every pair, we compare the values of the nodes in the pair:

- If the odd-indexed node is higher, the "Odd" team gets a point.
- If the even-indexed node is higher, the "Even" team gets a point.
Return the name of the team with the higher points, if the points are equal, return "Tie".
"""

from typing import Optional

from model import ListNode


class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        if head is None:
            return "Tie"
        if head.next is None:
            raise Exception("invalid argument")  # odd length not allowed

        even, odd = 0, 0

        curr = head

        while curr is not None and curr.next is not None:
            if curr.val > curr.next.val:
                even += 1
            else:
                odd += 1
            curr = curr.next.next

        if curr is not None:
            raise Exception("invalid argument")  # odd length not allowed

        if odd > even:
            return "Odd"
        elif odd < even:
            return "Even"
        else:
            return "Tie"
