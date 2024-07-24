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

from typing import Optional, Tuple, cast


class Node:
    """Definition for a Node."""

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        node = Node(insertVal)
        if head is None:
            head = node
            head.next = head
        elif head.next == head:
            head.next = node
            node.next = head
        else:
            min_node, max_node = self.find_max_min_node(head)
            if min_node == max_node:
                next_node = head.next
                head.next = node
                node.next = next_node
            else:
                dummy_head = Node(1)
                dummy_head.next = min_node
                prev = dummy_head
                curr = min_node
                while curr is not None:
                    if curr.val >= insertVal:  # type: ignore
                        break
                    prev = prev.next  # type: ignore
                    curr = curr.next
                prev.next = node  # type: ignore
                node.next = curr
                max_node.next = dummy_head.next

        return head

    def find_max_min_node(self, head: "Node") -> Tuple["Node", "Node"]:
        min_node, max_node = head, head
        curr = head.next

        while curr != head:
            if curr.val <= min_node.val:  # type: ignore
                min_node = curr
            if curr.val >= max_node.val:  # type: ignore
                max_node = curr

            curr = cast(Node, curr).next

        return cast(Node, min_node), cast(Node, max_node)
