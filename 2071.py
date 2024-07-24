"""
2071. Maximum Number of Tasks You Can Assign

You have n tasks and m workers. Each task has a strength requirement stored in
a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength
to complete. The strength of each worker is stored in a 0-indexed integer array
workers, with the jth worker having workers[j] strength. Each worker can only
be assigned to a single task and must have a strength greater than or equal to
the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's
strength by strength. You can decide which workers receive the magical pills,
however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and
strength, return the maximum number of tasks that can be completed.
"""

from typing import List


class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        tasks.sort()
        workers.sort()

        i, j = 0, len(workers) - 1
        tasks_completed = 0
        while i < len(tasks) and j >= 0:
            if workers[j] >= tasks[i]:
                tasks_completed += 1
                i += 1
                j -= 1
            elif pills > 0 and workers[j] + strength >= tasks[i]:
                pills -= 1
                tasks_completed += 1
                i += 1
                j -= 1
            else:
                break

        while i >= 0 and j >= 0:
            if workers[i] >= tasks[j]:
                i -= 1
                j -= 1
            else:
                if pills > 0:
                    workers[i] += strength
                    pills -= 1
                    if workers[i] >= tasks[j]:
                        i -= 1
                        j -= 1
                    else:
                        break
                else:
                    break

        return max(len(tasks) - (j + 1), tasks_completed)
