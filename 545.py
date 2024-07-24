"""
545. Boundary of Binary Tree

The boundary of a binary tree is the concatenation of the root, the left
boundary, the leaves ordered from left-to-right, and the reverse order of the
right boundary.

The left boundary is the set of nodes defined by the following:
- The root node's left child is in the left boundary. If the root does not
  have a left child, then the left boundary is empty.
- If a node in the left boundary and has a left child, then the left child is
  in the left boundary.
- If a node is in the left boundary, has no left child, but has a right
  child, then the right child is in the left boundary.
- The leftmost leaf is not in the left boundary.
- The right boundary is similar to the left boundary, except it is the right
  side of the root's right subtree. Again, the leaf is not part of the right
  boundary, and the right boundary is empty if the root does not have a right
  child.

The leaves are nodes that do not have any children. For this problem,
the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.
"""

from typing import Optional, List, Set

from model import TreeNode


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node: Optional[TreeNode], buf: List[int], direction: int) -> None:
            nonlocal visited

            if node is None:
                return
            if node.left is None and node.right is None:
                return

            if node not in visited:
                buf.append(node.val)
                visited.add(node)

            if direction == 0:
                if node.left is not None:
                    traverse(node.left, buf, direction)
                else:
                    traverse(node.right, buf, direction)
            else:
                if node.right is not None:
                    traverse(node.right, buf, direction)
                else:
                    traverse(node.left, buf, direction)

        def leaf_nodes(node: Optional[TreeNode], buf: List[int]) -> None:
            if node is None:
                return
            if node.left is None and node.right is None:
                if node not in visited:
                    buf.append(node.val)
                    visited.add(node)
                return
            leaf_nodes(node.left, buf)
            leaf_nodes(node.right, buf)

        nodes: List[int] = []
        visited: Set[TreeNode] = set()

        traverse(root, nodes, 0)
        leaf_nodes(root, nodes)
        right_nodes: List[int] = []
        traverse(root, right_nodes, 1)
        nodes.extend(right_nodes[::-1])

        return nodes
