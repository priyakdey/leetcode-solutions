"""
1634. Add Two Polynomials Represented as Linked Lists

A polynomial linked list is a special type of linked list where every node 
represents a term in a polynomial expression.

Each node has three attributes:
- coefficient: an integer representing the number multiplier of the term. 
  The coefficient of the term 9x4 is 9.
- power: an integer representing the exponent. The power of the term 9x4 is 4.
- next: a pointer to the next node in the list, or null if it is the last 
  node of the list.

For example, the polynomial 5x3 + 4x - 7 is represented by the polynomial 
linked list illustrated below:

The polynomial linked list must be in its standard form: the polynomial must be 
in strictly descending order by its power value. Also, terms with a coefficient 
of 0 are omitted.

Given two polynomial linked list heads, poly1 and poly2, add the polynomials 
together and return the head of the sum of the polynomials.

PolyNode format:

The input/output format is as a list of n nodes, where each node is represented 
as its [coefficient, power]. For example, the polynomial 5x3 + 4x - 7 would 
be represented as: [[5,3],[4,1],[-7,0]].

"""

from typing import Optional


class PolyNode:
    """Definition for polynomial singly-linked list."""

    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next


class Solution:
    def addPoly(
        self, poly1: "Optional[PolyNode]", poly2: "Optional[PolyNode]"
    ) -> "Optional[PolyNode]":
        if poly1 is None:
            return poly2

        if poly2 is None:
            return poly1

        curr1, curr2 = poly1, poly2

        head = PolyNode(-1, -1)
        curr = head

        while curr1 is not None and curr2 is not None:
            if curr1.power == curr2.power:
                if curr1.coefficient + curr2.coefficient == 0:
                    curr1 = curr1.next
                    curr2 = curr2.next
                    continue
                curr.next = PolyNode(curr1.coefficient + curr2.coefficient, curr1.power)
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1.power > curr2.power:
                curr.next = PolyNode(curr1.coefficient, curr1.power)
                curr1 = curr1.next
            else:
                curr.next = PolyNode(curr2.coefficient, curr2.power)
                curr2 = curr2.next
            curr = curr.next

        if curr1 is not None:
            curr.next = curr1
        if curr2 is not None:
            curr.next = curr2

        return head.next
