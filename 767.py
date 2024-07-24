"""
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
"""

from collections import Counter
from typing import Tuple, List


class MaxHeap:
    def __init__(self):
        self.elements: List[Tuple[str, int]] = []

    def push(self, ch: str, freq: int) -> None:
        self.elements.append((ch, freq))
        if len(self.elements) == 1:
            return

        curr_index = len(self.elements) - 1
        while curr_index > 0:
            parent_index = self.get_parent_index(curr_index)
            if self.__is_gt(curr_index, parent_index):
                self.__swap(curr_index, parent_index)
            else:
                break

            curr_index = parent_index

    def pop(self) -> Tuple[str, int]:
        root = self.elements[0]
        self.__swap(0, len(self.elements) - 1)
        self.elements.pop()

        curr_index = len(self.elements) - 1

        while curr_index > 0:
            left_index, right_index = self.get_parent_index(curr_index)
            if left_index >= len(self.elements):
                break

            swap_index = left_index
            if right_index < len(self.elements) and self.__is_gt(
                right_index, swap_index
            ):
                swap_index = right_index

            if self.__is_gt(curr_index, swap_index):
                self.__swap(curr_index, swap_index)
            else:
                break
            curr_index = swap_index

        return root

    def peek(self) -> Tuple[str, int]:
        return self.elements[0]

    def __len__(self) -> int:
        return len(self.elements)

    def __swap(self, i: int, j: int) -> None:
        self.elements[i], self.elements[j] = self.elements[j], self.elements[i]

    def __is_gt(self, i: int, j: int) -> bool:
        return self.elements[i][1] > self.elements[j][1]

    @staticmethod
    def get_parent_index(index: int) -> int:
        return (index - 1) // 2

    @staticmethod
    def get_child_index(index: int) -> Tuple[int, int]:
        return 2 * index + 1, 2 * index + 2


class Solution:
    def reorganizeString(self, s: str) -> str:
        if s is None or len(s) == 0:
            raise Exception("invalid arguments")
        if len(s) == 1:
            return s

        freq_map = Counter(s)
        heap = MaxHeap()
        for ch, freq in freq_map.items():
            heap.push(ch, freq)

        ch, balance = heap.pop()
        buf = [""] * len(s)

        for i in range(2 * balance, 2):
            buf[i] = ch

        curr = 1
        while len(heap) > 0:
            if balance < 2 and heap.peek()[1] == 1:
                break

            ch, freq = heap.pop()
            if balance == 0:
                balance += freq
            else:
                balance -= freq
            for _ in range(freq):
                buf[curr] = ch
                curr += 2

        if balance > 2:
            return ""

        while len(heap) > 0:
            ch, _ = heap.pop()
            buf[curr] = ch
            curr += 1

        return "".join(buf)
