"""
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
"""

from collections import Counter
from typing import List, Tuple


class MaxHeap:

    def __init__(self):
        self.heap: List[Tuple[str, int]] = []

    def push(self, ch: str, freq: int) -> None:
        self.heap.append((ch, freq))

        curr_index = len(self.heap) - 1
        while curr_index > 0:
            parent_index = (curr_index - 1) // 2
            if self.heap[curr_index][1] > self.heap[parent_index][1]:
                self.heap[curr_index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[curr_index],
                )
            else:
                break
            curr_index = parent_index

    def pop(self) -> Tuple[str, int]:
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        curr_index = 0
        while curr_index < len(self.heap):
            left_index = 2 * curr_index + 1
            right_index = 2 * curr_index + 2

            if left_index >= len(self.heap):
                break

            swap_index = left_index

            if (
                right_index < len(self.heap)
                and self.heap[right_index][1] > self.heap[left_index][1]
            ):
                swap_index = right_index

            if self.heap[swap_index][1] > self.heap[curr_index][1]:
                self.heap[swap_index], self.heap[curr_index] = (
                    self.heap[curr_index],
                    self.heap[swap_index],
                )
            else:
                break
            curr_index = swap_index

        return root

    def __len__(self):
        return len(self.heap)


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s)

        heap = MaxHeap()
        for ch, freq in freq_map.items():
            heap.push(ch, freq)

        buf: List[str] = []
        while len(heap) != 0:
            if len(heap) > 1:
                ch1, freq1 = heap.pop()
                ch2, freq2 = heap.pop()
                buf.append(ch1)
                buf.append(ch2)
                freq1 -= 1
                if freq1 > 0:
                    heap.push(ch1, freq1)
                freq2 -= 1
                if freq2 > 0:
                    heap.push(ch2, freq2)
            else:
                ch, freq = heap.pop()
                if freq > 1:
                    return ""
                buf.append(ch)

        return "".join(buf)
