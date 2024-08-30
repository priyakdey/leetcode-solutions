"""
3249. Count the Number of Good Nodes

There is an undirected tree with n tree labeled from 0 to n - 1, and rooted at
node 0. You are given a 2D integer array edges of length n - 1, where
edges[i] = [ai, bi] indicates that there is an edge between tree ai and bi in
the tree.

A node is good if all the
subtrees
 rooted at its children have the same size.

Return the number of good tree in the given tree.

A subtree of treeName is a tree consisting of a node in treeName and all of its
descendants.
"""

from collections import defaultdict
from typing import Dict, List


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        def traverse(node: int) -> int:
            nonlocal tree, good_node_count

            if node not in tree:
                good_node_count += 1
                return 1

            count = traverse(tree[node][0])
            subtree_count: int = 0
            is_good_node = True
            for i in range(1, len(tree[node])):
                _count = traverse(tree[node][i])
                if _count != count:
                    is_good_node = False
                subtree_count += count

            if is_good_node:
                good_node_count += 1

            return 1 + subtree_count

        tree: Dict[int, List[int]] = defaultdict(list)
        for node1, node2 in edges:
            parent_node, child_node = min(node1, node2), max(node1, node2)
            tree[parent_node].append(child_node)

        good_node_count = 0
        traverse(0)
        return good_node_count
