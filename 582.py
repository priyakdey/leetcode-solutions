"""
582. Kill Process

You have n processes forming a rooted tree structure. You are given two integer
arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i]
is the ID of the ith process's parent process.

Each process has only one parent process but may have multiple children
processes. Only one process has ppid[i] = 0, which means this process has no
parent process (the root of the tree).

When a process is killed, all of its children processes will also be killed.

Given an integer kill representing the ID of a process you want to kill, return
a list of the IDs of the processes that will be killed. You may return the
answer in any order.
"""

from collections import defaultdict
from typing import Dict, List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        def kill_process(process_id: int) -> List[int]:
            nonlocal process_graph

            if process_id not in process_graph:
                return [process_id]

            killed: List[int] = [process_id]

            for child in process_graph[process_id]:
                killed.extend(kill_process(child))

            return killed

        process_graph: Dict[int, List[int]] = defaultdict(list)

        for index, parent_pid in enumerate(ppid):
            process_graph[parent_pid].append(pid[index])

        return kill_process(kill)
