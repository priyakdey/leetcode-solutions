"""
502. IPO

Suppose LeetCode will start its IPO soon. In order to sell a good price of
its shares to Venture Capital, LeetCode would like to work on some projects
to increase its capital before the IPO. Since it has limited resources, it can
only finish at most k distinct projects before the IPO. Help LeetCode design the
best way to maximize its total capital after finishing at most k distinct
projects.

You are given n projects where the ith project has a pure profit profits[i]
and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its
pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize
your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.
"""

from typing import Callable, List, Tuple


class Heap:
    def __init__(self, compare_fn: Callable[[Tuple[int, int], Tuple[int, int]], bool]):
        self.heap: List[Tuple[int, int]] = []
        self.compare_fn = compare_fn

    def push(self, capital: int, profit: int) -> None:
        self.heap.append((capital, profit))

        curr_index = len(self.heap) - 1
        while curr_index > 0:
            parent_index = (curr_index - 1) // 2
            if self.compare_fn(self.heap[curr_index], self.heap[parent_index]):
                self.heap[curr_index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[curr_index],
                )
            else:
                break

            curr_index = parent_index

    def peek(self) -> Tuple[int, int]:
        return self.heap[0]

    def pop(self) -> Tuple[int, int]:
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        curr_index = 0
        while curr_index < len(self.heap):
            left_index, right_index = 2 * curr_index + 1, 2 * curr_index + 2

            if left_index >= len(self.heap):
                break

            swap_index = left_index
            if right_index < len(self.heap) and self.compare_fn(
                self.heap[right_index], self.heap[left_index]
            ):
                swap_index = right_index

            if self.compare_fn(self.heap[swap_index], self.heap[curr_index]):
                self.heap[curr_index], self.heap[swap_index] = (
                    self.heap[swap_index],
                    self.heap[curr_index],
                )
            else:
                break

            curr_index = swap_index

        return root

    def __len__(self) -> int:
        return len(self.heap)


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        lte: Callable[[Tuple[int, int], Tuple[int, int]], bool] = (
            lambda x, y: x[0] <= y[0]
        )
        gte: Callable[[Tuple[int, int], Tuple[int, int]], bool] = (
            lambda x, y: x[1] >= y[1]
        )

        starting_capital: int = w
        min_heap = Heap(lte)
        max_heap = Heap(gte)

        for capital, profit in zip(capital, profits):
            min_heap.push(capital, profit)

        for _ in range(k):
            # push all doable projects into max heap from min heap
            while len(min_heap) > 0 and min_heap.peek()[0] <= starting_capital:
                max_heap.push(*min_heap.pop())

            if len(max_heap) == 0:
                break

            # pop out the job with max profit
            _, profit = max_heap.pop()
            starting_capital = starting_capital + profit

        return starting_capital
