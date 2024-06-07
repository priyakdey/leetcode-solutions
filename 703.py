"""
703. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the 
kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

- KthLargest(int k, int[] nums) Initializes the object with the integer k and 
  the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element 
  representing the kth largest element in the stream.
"""

from typing import List, Tuple


class PriorityQueue:

    def __init__(self, capacity: int) -> None:
        self.items = [-1] * capacity
        self.length = 0
        self.capacity = capacity

    def push(self, num: int) -> None:
        self.items[self.length] = num
        self.length += 1

        curr_index = self.length - 1
        while curr_index > 0:
            parent_index = self.get_parent_index(curr_index)
            if self.items[curr_index] < self.items[parent_index]:
                self.swap(parent_index, curr_index)
            else:
                break

            curr_index = parent_index

    def pop(self) -> int:
        root = self.items[0]
        self.swap(0, self.length - 1)
        self.length -= 1

        curr_index = 0

        while curr_index < self.length:
            left_index, right_index = self.get_children_index(curr_index)

            if left_index >= self.length:
                break

            swap_index = left_index
            if (
                right_index < self.length
                and self.items[right_index] < self.items[left_index]
            ):
                swap_index = right_index

            if self.items[swap_index] < self.items[curr_index]:
                self.swap(curr_index, swap_index)
            else:
                break

            curr_index = swap_index

        return root

    def peek(self) -> int:
        return self.items[0]

    def is_full(self) -> bool:
        return self.length == self.capacity

    def __len__(self) -> int:
        return self.length

    def swap(self, i: int, j: int) -> None:
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def get_children_index(self, index: int) -> Tuple[int, int]:
        return 2 * index + 1, 2 * index + 2


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = PriorityQueue(k)

        for num in nums:
            if self.pq.is_full():
                if num > self.pq.peek():
                    self.pq.pop()
                    self.pq.push(num)
            else:
                self.pq.push(num)

    def add(self, val: int) -> int:
        if self.pq.is_full():
            if val > self.pq.peek():
                self.pq.pop()
                self.pq.push(val)
        else:
            self.pq.push(val)

        return self.pq.peek()
