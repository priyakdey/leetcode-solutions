"""
708. Insert into a Sorted Circular Linked List

Given a Circular Linked List node, which is sorted in non-descending order, 
write a function to insert a value insertVal into the list such that it remains 
a sorted circular list. The given node can be a reference to any single node 
in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place 
to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new 
single circular list and return the reference to that single 
node. Otherwise, you should return the originally given node.
"""

from typing import Optional, cast


class Node:
    """Definition for a Node."""

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        if head is None:
            return Node(insertVal)

        curr = head
        node = Node(insertVal)

        max_node = head
        min_node = head

        curr = head
        while curr.next is not head:
            if curr.val > max_node.val:
                max_node = curr
            if curr.val < min_node.val:
                min_node = curr
            curr = curr.next

        return head


head = Node(3)
head.next = Node(5)
head.next.next = Node(1)
head.next.next.next = head

Solution().insert(head, 0)
