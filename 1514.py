"""
1514. Path with Maximum Probability

You are given an undirected weighted graph of n nodes (0-indexed), represented
by an edge list where edges[i] = [a, b] is an undirected edge connecting the
nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of
success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted
if it differs from the correct answer by at most 1e-5.
"""
from collections import defaultdict, deque
from heapq import heappush, heappop
from typing import Deque, Dict, List, Tuple


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph: Dict[int, List[Tuple[int, float]]] = self.to_graph(edges, succProb)

        queue: Deque[Tuple[int, float]] = deque()
        queue.append((start_node, 1))
        heap: List[Tuple[int, float]] = []

        max_prob: float = 1.0

        while len(queue) > 0:
            node, prob = queue.popleft()
            if node == end_node:
                break

            max_prob *= prob

            for nbor, prob in graph[node]:
                heappush(heap, (nbor, -prob))
            node, prob = heappop(heap)
            queue.append((node, -prob))

        return max_prob


    def to_graph(self, edges: List[List[int]], succProb: List[float]) -> Dict[int, List[Tuple[int, float]]]:
        graph: Dict[int, List[Tuple[int, float]]] = defaultdict(list)
        for i, src, dest in enumerate(edges):
            graph[src].append((dest, succProb[i]))
            graph[dest].append((src, succProb[i]))

        return graph