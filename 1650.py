"""
1650. Lowest Common Ancestor of a Binary Tree III

Given two nodes of a binary tree p and q, return their lowest common ancestor 
(LCA).

Each node will have a reference to its parent node. The definition for Node 
is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

According to the definition of LCA on Wikipedia: "The lowest common ancestor 
of two nodes p and q in a tree T is the lowest node that has both p and q 
as descendants (where we allow a node to be a descendant of itself)."
"""

from collections import deque
from typing import Deque, Optional


class Node:
    """Definition for a Node."""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        if p == q:
            return p
        if p.parent is None:
            return p
        if q.parent is None:
            return q

        p_parents = self.get_parents(p)
        q_parents = self.get_parents(q)

        while p_parents[-1] != q_parents[-1]:
            if len(p_parents) > len(q_parents):
                p_parents.pop()
            elif len(p_parents) < len(q_parents):
                q_parents.pop()
            else:
                p_parents.pop()
                q_parents.pop()

        return p_parents[-1]

    def get_parents(self, node: Optional[Node]) -> Deque[Node]:
        dq = deque()

        while node is not None:
            dq.appendleft(node)
            node = node.parent

        return dq
