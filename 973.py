"""
973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the 
X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., √(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order. The answer is guaranteed to be unique 
(except for the order that it is in).
"""

from typing import List, Tuple


class PriorityQueue:

    def __init__(self, capacity: int) -> None:
        self.items: List[Tuple[List[int], int]] = [([0, 0], 0)] * capacity
        self.length = 0
        self.capacity = capacity

    def push(self, point: List[int], distance: int) -> None:
        self.items[self.length] = (point, distance)
        self.length += 1

        curr_index = self.length - 1
        while curr_index > 0:
            parent_index = self.get_parent_index(curr_index)
            if self.items[curr_index][1] > self.items[parent_index][1]:
                self.swap(parent_index, curr_index)
            else:
                break

            curr_index = parent_index

    def pop(self) -> Tuple[List[int], int]:
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
                and self.items[right_index][1] > self.items[left_index][1]
            ):
                swap_index = right_index

            if self.items[swap_index][1] > self.items[curr_index][1]:
                self.swap(curr_index, swap_index)
            else:
                break

            curr_index = swap_index

        return root

    def peek(self) -> Tuple[List[int], int]:
        return self.items[0]

    def is_full(self) -> bool:
        return self.length == self.capacity

    def is_empty(self) -> bool:
        return self.length == 0

    def __len__(self) -> int:
        return self.length

    def swap(self, i: int, j: int) -> None:
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def get_children_index(self, index: int) -> Tuple[int, int]:
        return 2 * index + 1, 2 * index + 2


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = PriorityQueue(k)

        for point in points:
            distance = self.calc_sq_distance(point)
            print(point, distance)
            if pq.is_full():
                if distance < pq.peek()[1]:
                    pq.pop()
                    pq.push(point, distance)
            else:
                pq.push(point, distance)

        closest_points = [[0, 0]] * k
        cursor = 0

        while not pq.is_empty():
            closest_points[cursor] = pq.pop()[0]
            cursor += 1

        return closest_points

    def calc_sq_distance(self, point: List[int]) -> int:
        [x, y] = point
        return x**2 + y**2
