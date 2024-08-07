"""
1474. Delete N Nodes After M Nodes of a Linked List
Link: https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/description/

You are given the head of a linked list and two integers m and n.

Traverse the linked list and remove some nodes in the following way:
- Start with the head as the current node.
- Keep the first m nodes starting with the current node.
- Remove the next n nodes
- Keep repeating steps 2 and 3 until you reach the end of the list.
- Return the head of the modified list after removing the mentioned nodes.

Constraints:

The number of nodes in the list is in the range [1, 104].
1 <= Node.val <= 106
1 <= m, n <= 1000

"""

from model import ListNode


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = head
        prev, curr = dummy_head, head

        while curr is not None:
            _m = m
            while curr is not None and _m > 0:
                prev.next = curr
                prev = curr
                curr = curr.next
                _m -= 1

            _n = n
            while curr is not None and _n > 0:
                curr = curr.next
                _n -= 1

        prev.next = None
        return dummy_head.next
