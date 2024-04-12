"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly 
with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other 
cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the 
ith city and the jth city are directly connected, and isConnected[i][j] = 0 
otherwise.

Return the total number of provinces.
"""

from typing import List, Set


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def _dfs(node: int) -> None:
            nonlocal visited

            for edge, value in enumerate(isConnected[node]):
                if edge not in visited and value == 1:
                    visited.add(edge)
                    _dfs(edge)

        n = len(isConnected)
        visited: Set[int] = set()

        provinces = 0
        for node, _ in enumerate(isConnected):
            if node not in visited:
                provinces += 1
                visited.add(node)
                _dfs(node)

        return provinces
