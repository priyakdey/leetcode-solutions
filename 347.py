"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.
"""

from collections import Counter
from typing import Dict, List, Tuple


class MaxHeap:

    def __init__(self):
        self.table: List[int] = []

    def push(self, num: int) -> None:
        self.table.append(num)

        curr_index = len(self.table) - 1

        while curr_index > 0:
            parent_index = self.get_parent_index(curr_index)
            if self.table[curr_index] > self.table[parent_index]:
                self.table[curr_index], self.table[parent_index] = (
                    self.table[parent_index],
                    self.table[curr_index],
                )
                curr_index = parent_index
            else:
                break

    def pop(self) -> int:
        if self.is_empty():
            raise Exception("empty stuff")

        root = self.table[0]
        self.table[0] = self.table[-1]
        self.table.pop()

        curr_index = 0
        length = len(self.table)
        while curr_index < length:
            left_index, right_index = self.get_children_index(curr_index)
            if left_index >= length:
                break

            swap_index = left_index
            if (
                right_index < length
                and self.table[right_index] > self.table[left_index]
            ):
                swap_index = right_index

            if self.table[swap_index] > self.table[curr_index]:
                self.table[swap_index], self.table[curr_index] = (
                    self.table[curr_index],
                    self.table[swap_index],
                )
                curr_index = swap_index
            else:
                break

        return root

    def is_empty(self) -> bool:
        return len(self.table) == 0

    def get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def get_children_index(self, index: int) -> Tuple[int, int]:
        return 2 * index + 1, 2 * index + 2


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = self.freq_to_element_map(nums)

        max_heap = MaxHeap()

        for freq in freq_count.keys():
            max_heap.push(freq)

        top_freq_elements: List[int] = []
        while k > 0:
            freq = max_heap.pop()
            elements = freq_count[freq]
            length = len(elements)

            if length <= k:
                top_freq_elements.extend(elements)
            else:
                top_freq_elements.extend(elements[:k])

            k -= length

        return top_freq_elements

    def freq_to_element_map(self, nums: List[int]) -> Dict[int, List[int]]:
        element_count = dict(Counter(nums))
        freq_count = {}
        for element, freq in element_count.items():
            if freq not in freq_count:
                freq_count[freq] = []
            freq_count[freq].append(element)

        return freq_count
