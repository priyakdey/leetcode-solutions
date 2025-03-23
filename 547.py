from collections import defaultdict, deque
from typing import Deque, List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph: Dict[int, List[int]] = defaultdict(list)

        for src in range(n):
            for dest in range(n):
                if isConnected[src][dest] == 1:
                    graph[src].append(dest)
                    graph[dest].append(src)

        visited: List[bool] = [False] * n
        queue: Deque[int] = deque()
        provinces = 0

        for city in range(n):
            if visited[city]:
                continue

            queue.append(city)
            visited[city] = True
            provinces += 1

            while len(queue) > 0:
                c = queue.popleft()

                for nbor in graph[c]:
                    if not visited[nbor]:
                        queue.append(nbor)
                        visited[nbor] = True

        return provinces
