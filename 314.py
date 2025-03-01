from collections import defaultdict, deque
from typing import Dict, List


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:

        def to_graph(edges: List[List[int]]) -> Dict[int, List[int]]:
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                if u != v:
                    graph[v].append(u)

            return graph

        def node_count_to_distance(graph: Dict[int, List[int]]) -> List[int]:
            """Returns a list of reachable nodes from each node at an even distance"""
            n = len(graph)
            reachable_nodes = [0] * n

            for start in range(n):
                visited = set()
                queue = deque([(start, 0)])

                while queue:
                    node, dist = queue.popleft()
                    if node in visited:
                        continue
                    visited.add(node)
                    if dist & 1 == 0:
                        reachable_nodes[start] += 1
                    for neighbor in graph[node]:
                        queue.append((neighbor, dist + 1))

            return reachable_nodes

        graph1 = to_graph(edges1)
        graph2 = to_graph(edges2)

        count1 = node_count_to_distance(graph1)
        count2 = node_count_to_distance(graph2)

        max_node_counts = [0] * len(graph1)
        for node1 in graph1:
            max_node_count = 0
            for node2 in graph2:
                max_node_count = max(max_node_count, count1[node1] + count2[node2])

            max_node_counts[node1] = max_node_count

        return max_node_counts
