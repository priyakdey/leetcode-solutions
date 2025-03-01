from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def index_of(num: int) -> int:
            nonlocal nums

            index = -1
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= num:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return index

        left_index = index_of(target)
        if left_index == -1 or nums[left_index] != target:
            return [-1, -1]

        right_index = index_of(target + 1)
        if right_index == -1 or right_index < left_index:
            return [left_index, len(nums) - 1]

        return [left_index, right_index - 1]
