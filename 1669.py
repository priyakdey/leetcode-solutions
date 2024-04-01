"""
1669. Merge In Between Linked Lists

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their 
place.

Build the result list and return its head.
"""


from model import ListNode


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        a_th_node, b_th_node = None, None

        curr = list1
        i = 0
        while curr is not None:
            if i == a - 1:
                a_th_node = curr
            elif i == b:
                b_th_node = curr
            i += 1
            curr = curr.next

        a_th_node.next = list2
        curr = list2
        while curr.next is not None:
            curr = curr.next
        curr.next = b_th_node.next

        return list1
