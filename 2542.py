from heapq import heapop, heappush
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def traverse(index: int, total: int, heap: List[int]) -> None:
            nonlocal num1, nums2, k, max_score

            if len(heap) == k:
                max_score = max(max_score, total * heap[0])
                return

            if index == len(nums1):
                return

            traverse(index, total, heap)
            heappush(heap, nums2[index])
            traverse(index + 1, total + nums1[index], heap)
            heappop(heap)

        max_score = 0
        traverse(0, 0, [])
        return max_score
