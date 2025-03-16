from collections import deque
from typing import Deque, List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: List[List[int]] = [[] for _ in range(numCourses)]
        indegrees: List[int] = [0] * numCourses
        for [course, pre] in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1

        queue: Deque[int] = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)

        completed_courses = 0

        while len(queue) > 0:
            course = queue.popleft()
            completed_courses += 1

            for nbor in graph[course]:
                indegrees[nbor] -= 1
                if indegrees[nbor] == 0:
                    queue.append(nbor)

        return completed_courses == numCourses
