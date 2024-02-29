"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.
"""

from typing import Dict, List


class MaxHeap:
    def __init__(self):
        self.data = []

    # HElPERS
    def parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    # END - HElPERS

    def push(self, value: int) -> None:
        self.data.append(value)

        # now heapify the array from bottom up
        curr_index = len(self.data) - 1
        while curr_index > 0:
            parent_index = self.parent_index(curr_index)

            if self.data[curr_index] > self.data[parent_index]:
                temp = self.data[curr_index]
                self.data[curr_index] = self.data[parent_index]
                self.data[parent_index] = temp
            else:
                break

            curr_index = parent_index

    def pop(self) -> int:
        max_element = self.data[0]

        # now heapify the array
        # copy last element to root
        self.data[0] = self.data[-1]
        self.data = self.data[:-1]

        # move from top down and swap if necessary
        curr_index = 0
        while curr_index < len(self.data):
            left_child_index, right_child_index = self.left_child_index(
                curr_index
            ), self.right_child_index(curr_index)

            if left_child_index >= len(self.data):
                # curr_index = last index
                break

            # decide which child to swap with if necessary
            swap_index = left_child_index
            if (
                right_child_index < len(self.data)
                and self.data[right_child_index] > self.data[left_child_index]
            ):
                swap_index = right_child_index

            if self.data[swap_index] > self.data[curr_index]:
                temp = self.data[swap_index]
                self.data[swap_index] = self.data[curr_index]
                self.data[curr_index] = temp
            else:
                break

            curr_index = swap_index

        return max_element


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # generate the freq map Dict[int, int] {num -> freq}
        number_freq_map: Dict[int, int] = {}
        for num in nums:
            if num in number_freq_map:
                number_freq_map[num] += 1
            else:
                number_freq_map[num] = 1

        # lets group the numbers by its freq
        # this needs to be Dict[int, List[int]]
        freq_number_map: Dict[int, List[int]] = {}

        for num, count in number_freq_map.items():
            if count in freq_number_map:
                freq_number_map[count].append(num)
            else:
                freq_number_map[count] = [num]

        heap = MaxHeap()
        for count in freq_number_map.keys():
            heap.push(count)

        top_freq_elements = []
        while k != 0:
            count = heap.pop()
            elements = freq_number_map[count]
            top_freq_elements.extend(elements)
            k -= len(elements)

        return top_freq_elements
