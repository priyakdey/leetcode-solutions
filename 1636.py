"""
1636. Sort Array by Increasing Frequency

Given an array of integers nums, sort the array in increasing order based on
the frequency of the values. If multiple values have the same frequency,
sort them in decreasing order.

Return the sorted array.
"""

from collections import Counter
from typing import List, Tuple


def get_child_index(index: int) -> Tuple[int, int]:
    return 2 * index + 1, 2 * index + 2


class MinHeap:

    def __init__(self, capacity: int):
        self.elements: List[Tuple[int, int]] = [(0, 0)] * capacity
        self.length = 0
        self.capacity = capacity

    def push(self, val: int, freq: int) -> None:
        if self.length == self.capacity:
            raise Exception("overflow")

        self.elements[self.length] = (val, freq)
        curr_index = self.length
        self.length += 1

        while curr_index > 0:
            parent_index = self.get_parent_index(curr_index)
            if self.elements[curr_index][1] < self.elements[parent_index][1]:
                self.swap(curr_index, parent_index)
            elif (
                self.elements[curr_index][1] == self.elements[parent_index][1]
                and self.elements[curr_index][0] > self.elements[parent_index][0]
            ):
                self.swap(curr_index, parent_index)
            else:
                break
            curr_index = parent_index

    def pop(self) -> Tuple[int, int]:
        if self.length == 0:
            raise Exception("underflow")

        root = self.elements[0]
        self.swap(0, self.length - 1)
        self.length -= 1
        curr_index = 0

        while curr_index < self.length:
            left_index, right_index = self.get_child_index(curr_index)

            if left_index >= self.length:
                break

            swap_index = left_index

            if (
                right_index < self.length
                and self.elements[right_index][1] < self.elements[left_index][1]
            ):
                swap_index = right_index
            elif (
                right_index < self.length
                and self.elements[right_index][1] == self.elements[left_index][1]
                and self.elements[right_index][0] == self.elements[left_index][0]
            ):
                swap_index = right_index

            if self.elements[curr_index][1] < self.elements[swap_index][1]:
                self.swap(curr_index, swap_index)
            elif (
                self.elements[curr_index][1] == self.elements[swap_index][1]
                and self.elements[curr_index][0] > self.elements[swap_index][0]
            ):
                self.swap(curr_index, swap_index)
            else:
                break

            curr_index = swap_index

        return root

    def is_empty(self) -> bool:
        return self.length == 0

    @staticmethod
    def get_parent_index(index: int) -> int:
        return (index - 1) // 2

    @staticmethod
    def get_child_index(index: int) -> Tuple[int, int]:
        return 2 * index + 1, 2 * index + 2

    def swap(self, i: int, j: int) -> None:
        self.elements[i], self.elements[j] = self.elements[j], self.elements[i]


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_map = Counter(nums)
        heap = MinHeap(len(freq_map))
        for val, freq in freq_map.items():
            heap.push(val, freq)

        cursor = 0
        while not heap.is_empty():
            val, freq = heap.pop()
            for i in range(freq):
                nums[cursor] = val
                cursor += 1
        return nums
