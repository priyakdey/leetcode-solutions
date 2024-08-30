"""
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

A critical point in a linked list is defined as either a local maxima or a
local minima.

A node is a local maxima if the current node has a value strictly greater than
the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller
than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a
previous node and a next node.

Given a linked list head, return an array of length 2 containing
[minDistance, maxDistance] where minDistance is the minimum distance between
any two distinct critical points and maxDistance is the maximum distance
between any two distinct critical points. If there are fewer than two
critical points, return [-1, -1].
"""
from typing import List, Optional

from model import ListNode


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        indices: List[int] = []

        prev, curr = head, head.next
        index = 1

        while curr.next is not None:
            if prev.val < curr.val > curr.next.val or prev.val > curr.val < curr.next.val:
                indices.append(index)
            index += 1
            prev = curr
            curr = curr.next

        if len(indices) < 2:
            return [-1, -1]

        min_distance = (1 << 31) - 1
        for i in range(1, len(indices)):
            min_distance = min(min_distance, indices[i] - indices[i - 1])

        return [min_distance, indices[-1] - indices[0]]

