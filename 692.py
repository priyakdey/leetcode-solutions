"""
692. Top K Frequent Words

Given an array of strings words and an integer k, return the k most frequent
strings.

Return the answer sorted by the frequency from highest to lowest. Sort the
words with the same frequency by their lexicographical order.
"""

from collections import Counter
from typing import List, Tuple


class MinHeap:

    def __init__(self, capacity: int):
        self.heap: List[Tuple[str, int]] = [("", -1)] * capacity
        self.length = 0
        self.capacity = capacity

    def push(self, word: str, freq: int) -> None:
        if self.length == self.capacity:
            raise Exception("overflow")

        curr_index = self.length
        self.heap[curr_index] = (word, freq)
        self.length += 1

        if self.length == 1:
            return

        while curr_index > 0:
            parent_index = self.__get_parent_index(curr_index)
            if self.__is_lt(curr_index, parent_index):
                self.__swap(curr_index, parent_index)
            else:
                break

            curr_index = parent_index

    def pop(self) -> Tuple[str, int]:
        if self.length == 0:
            raise Exception("underflow")

        root = self.heap[0]
        self.__swap(0, self.length - 1)
        self.length -= 1

        if self.length != 0:
            curr_index = 0

            while curr_index < self.length:
                left_index, right_index = self.__get_child_index(curr_index)

                if left_index >= self.length:
                    break

                swap_index = left_index
                if right_index < self.length and self.__is_lt(right_index, swap_index):
                    swap_index = right_index

                if self.__is_lt(swap_index, curr_index):
                    self.__swap(curr_index, swap_index)
                else:
                    break

                curr_index = swap_index

        return root

    def peek(self) -> Tuple[str, int]:
        if self.length == 0:
            raise Exception("underflow")
        return self.heap[0]

    def __len__(self) -> int:
        return self.length

    def __is_lt(self, i: int, j: int) -> bool:
        if self.heap[i][1] < self.heap[j][1]:
            return True
        elif self.heap[i][1] == self.heap[j][1]:
            return self.heap[i][0] > self.heap[j][0]
        else:
            return False

    @staticmethod
    def __get_parent_index(index: int) -> int:
        return (index - 1) // 2

    @staticmethod
    def __get_child_index(index: int) -> Tuple[int, int]:
        return 2 * index + 1, 2 * index + 2

    def __swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = MinHeap(k)

        for word, freq in counter.items():
            if len(heap) < k:
                heap.push(word, freq)
            else:
                _word, _freq = heap.peek()
                if freq > _freq or (freq == _freq and word < _word):
                    heap.pop()
                    heap.push(word, freq)

        most_common = [""] * k
        curr = k - 1

        while len(heap) > 0:
            most_common[curr], _ = heap.pop()
            curr -= 1

        return most_common
