from collections import defaultdict, deque
from typing import Deque, List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph: Dict[int, List[int]] = defaultdict(list)

        for src, dest in connections:
            graph[src].append(dest)
            graph[dest].append(src)

        visited: List[bool] = [False] * n
        queue: Deque[int] = deque()
        queue.append(0)
        visited[0] = True

        reverse = 0

        while len(queue) > 0:
            city = queue.popleft()

            for nbor in graph[city]:
                if nbor in visited:
                    continue

                if city in graph[nbor]:
                    reverse += 1
                queue.append(city)
                visited[city] = True

        return reverse
