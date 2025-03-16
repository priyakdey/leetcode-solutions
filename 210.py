from collections import deque
from typing import Deque, List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph: List[List] = [[] for _ in range(numCourses)]
        indegrees: List[int] = [0] * numCourses

        for [course, pre] in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1

        queue: Deque[int] = deque()

        queue: Deque[int] = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)

        order: List[int] = []
        completed = 0

        while len(queue) > 0:
            course = queue.popleft()
            completed += 1
            order.append(course)

            for nbor in graph[course]:
                indegrees[nbor] -= 1
                if indegrees[nbor] == 0:
                    queue.append(nbor)

        return order if completed == numCourses else []
