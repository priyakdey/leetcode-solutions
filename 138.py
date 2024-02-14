"""
138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional 
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n 
brand new nodes, where each new node has its value set to the value of its 
corresponding original node. Both the next and random pointer of the new nodes 
should point to new nodes in the copied list such that the pointers in the 
original list and copied list represent the same list state. None of the 
pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, 
where X.random --> Y, then for the corresponding two nodes x and y in the 
copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) that the random 
  pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

"""

from typing import Dict, Optional


class Node:
    def __init__(
        self, x: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        old_node_to_new_node_map: Dict["Node", "Node"] = {}

        cloned_head = None
        iter1, iter2 = head, None

        while iter1 is not None:
            node = Node(iter1.val)
            if iter1 is head:
                cloned_head = node
                iter2 = cloned_head
            else:
                iter2.next = node
                iter2 = iter2.next

            old_node_to_new_node_map[iter1] = node
            iter1 = iter1.next

        iter1, iter2 = head, cloned_head

        while iter1 is not None:
            random_ptr = iter1.random
            if random_ptr is not None:
                iter2.random = old_node_to_new_node_map[random_ptr]

            iter1 = iter1.next
            iter2 = iter2.next

        return cloned_head
