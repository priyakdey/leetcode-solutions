"""
3263. Convert Doubly Linked List to Array I

You are given the head of a doubly linked list, which contains nodes that have a
next pointer and a previous pointer.

Return an integer array which contains the elements of the linked list in order.
"""
from typing import List, Optional


class Node:
    """Definition for a Node."""
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next



class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        curr = root
        arr: List[int] = []

        while curr is not None:
            arr.append(curr.val)
            curr = curr.next

        return arr
