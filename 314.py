"""
314. Binary Tree Vertical Order Traversal

Given the root of a binary tree, return the vertical order traversal of its 
nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to 
right.

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

"""

from collections import deque
from typing import Deque, List, Optional, Tuple

from model import TreeNode


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]

        queue: Deque[Tuple[TreeNode, int]] = deque()
        queue.append((root, 0))

        mid_cursor = 0
        levels: List[List[int]] = [[]]

        while len(queue) != 0:
            node, level = queue.popleft()
            if level == 0:
                levels[mid_cursor].append(node.val)
            elif level < 0:
                if mid_cursor + level >= 0:
                    levels[mid_cursor + level].append(node.val)
                else:
                    levels.insert(0, [node.val])
                    mid_cursor += 1
            else:
                if mid_cursor + level < len(levels):
                    levels[mid_cursor + level].append(node.val)
                else:
                    levels.append([node.val])

            if node.left is not None:
                queue.append((node.left, level - 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

        return levels
