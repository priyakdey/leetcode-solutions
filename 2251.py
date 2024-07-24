"""
2251. Number of Flowers in Full Bloom

You are given a 0-indexed 2D integer array flowers, where
flowers[i] = [starti, endi] means the ith flower will be in full bloom from
starti to endi (inclusive). You are also given a 0-indexed integer array
people of size n, where people[i] is the time that the ith person will arrive
to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of
flowers that are in full bloom when the ith person arrives.
"""

from typing import List


class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        start_times = sorted(start for start, _ in flowers)
        end_times = sorted(end for _, end in flowers)

        flower_count = [0] * len(people)

        for i, person in enumerate(people):
            bloom_count = self.count_less_than_eq(start_times, person)
            dead_count = self.count_less_than(end_times, person)
            flower_count[i] = bloom_count - dead_count

        return flower_count

    def count_less_than_eq(self, arr: List[int], value: int) -> int:
        """returns the number of elements less and equals to the value"""
        index = -1
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] <= value:
                index = mid
                left = mid + 1
            else:
                right = mid - 1

        return index - 0 + 1

    def count_less_than(self, arr: List[int], value: int) -> int:
        """returns the number of elements less than value"""
        index = -1
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < value:
                index = mid
                left = mid + 1
            else:
                right = mid - 1

        return index - 0 + 1

    def naive_solution_fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        ans = []
        for person in people:
            flower = 0
            for start, end in flowers:
                if person in range(start, end + 1):
                    flower += 1

            ans.append(flower)

        return ans
