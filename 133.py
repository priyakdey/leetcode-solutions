"""
133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2,
and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite
graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the
copy of the given node as a reference to the cloned graph.
"""

from typing import Dict, Optional


class Node:
    """Definition for a Node."""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        def clone_node(node: Optional[Node]) -> Optional[Node]:
            nonlocal clones

            if node is None:
                return None

            if node in clones:
                return clones[node]

            clone = Node(node.val)
            clones[node] = clone

            for neighbor in node.neighbors:
                clone_neighbor = clone_node(neighbor)
                clone.neighbors.append(clone_neighbor)

            return clone

        if node is None:
            return None

        clones: Dict[Node, Node] = {}
        clone_node(node)
        return clones[node]
