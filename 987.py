"""
987. Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, calculate the vertical order traversal of the 
binary tree.

For each node at position (row, col), its left and right children will be at 
positions (row + 1, col - 1) and (row + 1, col + 1) respectively. 
The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom 
orderings for each column index starting from the leftmost column and ending 
on the rightmost column. There may be multiple nodes in the same row and same 
column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
"""

from collections import deque
from typing import Deque, List, Optional, Tuple

from model import TreeNode


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]

        queue: Deque[Tuple[TreeNode, int]] = deque()
        queue.append((root, 0))
        level_order: List[List[int]] = [[]]
        mid = 0

        while len(queue) != 0:
            node, offset = queue.popleft()

            if offset == 0:
                level_order[mid].append(node.val)
            elif offset > 0:
                # find number of elements b/w last element and mid
                count = (len(level_order) - 1) - (mid + 1) + 1
                if offset <= count:
                    level_order[mid + offset].append(node.val)
                else:
                    level_order.append([node.val])
            else:
                # find number of elements b/w first element and mid
                count = (mid - 1) - 0
                if offset <= count:
                    level_order[mid + offset].append(node.val)
                else:
                    level_order.append([node.val])

            if node.left is not None:
                queue.append((node.left, offset - 1))
            if node.right is not None:
                queue.append((node.right, offset + 1))

        return level_order
