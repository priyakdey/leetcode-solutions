"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] =
[ai, bi] indicates that you must take course bi first if you want to take
course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from collections import defaultdict, deque
from typing import Deque, Dict, List, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: Dict[int, Set[int]] = defaultdict(set)
        indegrees: List[int] = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].add(course)
            indegrees[course] += 1

        queue: Deque[int] = deque()

        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)

        courses_completed: int = 0

        while len(queue) > 0:
            course = queue.popleft()
            courses_completed += 1

            if course not in graph:
                continue

            for c in graph[course]:
                indegrees[c] -= 1
                if indegrees[c] == 0:
                    queue.append(c)

        return courses_completed == numCourses
