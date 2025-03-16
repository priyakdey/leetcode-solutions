from collections import defaultdict
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming: List[bool] = [False] * n

        for [src, dest] in edges:
            incoming[dest] = True

        result: List[int] = []
        for i, has_incoming in enumerate(incoming):
            if not has_incoming:
                result.append(i)

        return result
