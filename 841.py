from collections import deque
from typing import Deque, List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        length = len(rooms)
        visited: List[bool] = [False] * length
        queue: Deque[int] = deque()
        queue.append(0)
        visited[0] = True
        count = 1

        while len(queue) > 0:
            room = queue.popleft()

            for key in rooms[room]:
                if not visited[key]:
                    queue.append(key)
                    visited[key] = True
                    count += 1

        return count == length
