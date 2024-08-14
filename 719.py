"""
719. Find K-th Smallest Pair Distance

The distance of a pair of integers a and b is defined as the absolute difference
between a and b.

Given an integer array nums and an integer k, return the kth smallest distance
among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
"""
from typing import List, Tuple


class MaxHeap:

    def __init__(self, capacity: int):
        self.elements: List[Tuple[int, int, int]] = [(-1, -1, -1)] * capacity
        self.capacity = capacity
        self.length = 0

    def push(self, x: int, y: int, dist: int) -> None:
        self.elements[self.length] = (x, y, dist)
        self.length += 1

        curr_index = self.length - 1
        while curr_index > 0:
            parent_index = (curr_index - 1) // 2
            if self.__gt(curr_index, parent_index):
                self.__swap(curr_index, parent_index)
            else:
                break
            curr_index = parent_index

    def pop(self) -> Tuple[int, int, int]:
        root = self.elements[0]
        self.__swap(0, self.length - 1)
        self.length -= 1

        curr_index = 0
        while curr_index < self.length:
            left_index, right_index = 2 * curr_index + 1, 2 * curr_index + 2

            if left_index >= self.length:
                break

            swap_index = left_index
            if right_index < self.length and self.__gt(right_index, left_index):
                swap_index = right_index

            if self.__gt(swap_index, curr_index):
                self.__swap(swap_index, curr_index)
            else:
                break
            curr_index = swap_index

        return root

    def peek(self) -> Tuple[int, int, int]:
        return self.elements[0]

    def __len__(self) -> int:
        return self.length

    def __gt(self, i: int, j: int) -> bool:
        return self.elements[i][2] > self.elements[j][2]

    def __swap(self, i: int, j: int) -> None:
        self.elements[i], self.elements[j] = self.elements[j], self.elements[i]


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        heap = MaxHeap(k)

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                x, y = nums[i], nums[j]
                dist = abs(x - y)
                if len(heap) < k:
                    heap.push(x, y, dist)
                elif dist < heap.peek()[2]:
                    heap.pop()
                    heap.push(x, y, dist)

        return heap.peek()[2]
