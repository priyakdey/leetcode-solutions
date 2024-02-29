"""
239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size 
k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window 
moves right by one position.

Return the max sliding window.
"""

from collections import deque
from typing import Deque, List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue: Deque[int] = deque()

        for i in range(k):
            num = nums[i]
            while len(queue) != 0 and num > queue[-1]:
                queue.pop()

            queue.append(num)

        max_numbers = [0 for _ in range(len(nums) - k + 1)]
        max_numbers[0] = queue[0]
        cursor = 1

        for i in range(k, len(nums)):
            if queue[0] == nums[i - k]:
                queue.popleft()

            num = nums[i]
            while len(queue) != 0 and num > queue[-1]:
                queue.pop()

            queue.append(num)
            max_numbers[cursor] = queue[0]
            cursor += 1

        return max_numbers
