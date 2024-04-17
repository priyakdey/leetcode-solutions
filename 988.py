"""
988. Smallest String Starting From Leaf

You are given the root of a binary tree where each node has a value in the range 
[0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this 
tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.
"""

from typing import List, Optional
from model import TreeNode


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def traverse(node: TreeNode, buffer: List[str]) -> None:
            nonlocal smallest_string

            buffer.insert(0, chr(node.val + 97))

            if node.left is None and node.right is None:
                s = "".join(buffer)
                if smallest_string == "":
                    smallest_string = s
                else:
                    smallest_string = min(smallest_string, s)

                buffer.pop(0)
                return

            if node.left is not None : traverse(node.left, buffer)
            if node.right is not None: traverse(node.right, buffer)

            buffer.pop(0)

        smallest_string = ""

        if root is not None:
            traverse(root, [])

        return smallest_string

