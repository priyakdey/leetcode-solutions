"""
179. Largest Number

Given a list of non-negative integers nums, arrange them such that they form the
largest number and return it.

Since the result may be very large, so you need to return a string instead of an
integer.
"""

from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"

        arr: List[str] = [str(num) for num in nums]
        self.sort(arr, 0, len(arr) - 1)
        return "".join(arr)

    def sort(self, arr: List[str], left: int, right: int) -> None:
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.sort(arr, left, mid)
        self.sort(arr, mid + 1, right)
        self.merge(arr, left, mid, mid + 1, right)

    def merge(
        self,
        arr: List[str],
        left_start: int,
        left_end: int,
        right_start: int,
        right_end: int,
    ) -> None:
        left_length = left_end - left_start + 1
        right_length = right_end - right_start + 1

        merged_arr = [""] * (left_length + right_length)

        i, j, k = left_start, right_start, 0
        while i <= left_end and j <= right_end:
            if arr[j] + arr[i] > arr[i] + arr[j]:
                merged_arr[k] = arr[j]
                j += 1
            else:
                merged_arr[k] = arr[i]
                i += 1
            k += 1

        while i <= left_end:
            merged_arr[k] = arr[i]
            i += 1
            k += 1

        while j <= right_end:
            merged_arr[k] = arr[j]
            j += 1
            k += 1

        k = 0
        for i in range(left_start, left_end + 1):
            arr[i] = merged_arr[k]
            k += 1
        for i in range(right_start, right_end + 1):
            arr[i] = merged_arr[k]
            k += 1
