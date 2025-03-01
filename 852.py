from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                index = mid
                break
            elif arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return index

        
