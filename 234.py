"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome 
or false otherwise.
"""

from typing import Optional

from model import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        mid = self.find_mid(head.next, head)
        next_node = mid.next
        mid.next = None
        head2 = self.reverse_list(next_node, None)
        return self.is_palindrome(head, head2)

    def is_palindrome(
        self, curr1: Optional[ListNode], curr2: Optional[ListNode]
    ) -> bool:
        if curr1 is None or curr2 is None:
            return True

        return curr1.val == curr2.val and self.is_palindrome(curr1.next, curr2.next)

    def find_mid(self, curr: Optional[ListNode], mid: ListNode) -> ListNode:
        if curr is None or curr.next is None:
            return mid
        return self.find_mid(curr.next.next, mid.next)

    def reverse_list(self, curr: ListNode, prev: Optional[ListNode]) -> ListNode:
        if curr is None:
            return prev
        next_node = curr.next
        curr.next = prev
        return self.reverse_list(next_node, curr)
