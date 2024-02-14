"""
1823. Find the Winner of the Circular Game

There are n friends that are playing a game. The friends are sitting in a circle
and are numbered from 1 to n in clockwise order. More formally, moving clockwise 
from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving 
clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
- Count the next k friends in the clockwise direction including the friend you 
  started at. The counting wraps around the circle and may count some friends 
  more than once.
- The last friend you counted leaves the circle and loses the game.
- If there is still more than one friend in the circle, go back to step 2 
  starting from the friend immediately clockwise of the friend who just lost 
  and repeat.
- Else, the last friend in the circle wins the game.

Given the number of friends, n, and an integer k, return the winner of the game.

"""

# TODO: Solve this without the extra space


class ListNode:
    """represents a node in a double linked list"""

    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

    @staticmethod
    def generate_list(n: int) -> "ListNode":
        head = ListNode(1)
        curr = head
        for i in range(2, n + 1):
            node = ListNode(i)
            curr.next = node
            node.prev = curr
            curr = node

        curr.next = head
        head.prev = curr
        return head


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        head = ListNode.generate_list(n)
        return self.simulate(head, k)

    def simulate(self, node: ListNode, k: int) -> int:
        if node.next is node and node.prev is node:
            return node.val

        count = 1
        curr = node
        while count < k:
            curr = curr.next
            count += 1

        next_node = curr.next
        prev_node = curr.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        return self.simulate(next_node, k)
