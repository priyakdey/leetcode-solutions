from typing import List


class MinHeap:

    def __init__(self, capacity: int):
        self.elements: List[int] = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def offer(self, value: int) -> None:
        assert self.size < self.capacity

        self.elements[self.size] = value
        self.size += 1

        curr = self.size - 1
        while curr > 0:
            parent = (curr - 1) // 2
            if self.elements[curr] < self.elements[parent]:
                self.elements[curr], self.elements[parent] = (
                    self.elements[swap],
                    self.elements[curr],
                )
            else:
                break

            curr = parent

    def poll(self) -> int:
        assert self.size > 0

        root = self.elements[0]
        self.elements[0] = self.elements[self.size - 1]
        self.size -= 1

        curr = 0
        while curr < self.size:
            left, right = 2 * curr + 1, 2 * curr + 2

            if left >= self.size:
                break

            swap = left
            if right < self.size and self.elements[right] < self.elements[left]:
                swap = right

            if self.elements[swap] < self.elements[curr]:
                self.elements[curr], self.elements[swap] = (
                    self.elements[parent],
                    self.elements[curr],
                )
            else:
                break

            curr = swap

        return root

    def peek(self) -> int:
        assert self.size > 0
        return self.elements[0]

    def __len__(self) -> int:
        return self.size


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap(k)
        for num in nums:
            if len(heap) < k:
                heap.offer(num)
            elif heap.peek() < num:
                heap.poll()
                heap.offer(num)

        return heap.peek()
