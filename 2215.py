from typing import List, Set


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        def find_diff(arr: List[int], distinct_elements: Set) -> List[int]:
            result: Set[int] = set()
            for num in arr:
                if num not in distinct_elements:
                    result.add(num)

            return list(result)

        return [find_diff(nums1, set(nums2)), find_diff(nums2, set(nums1))]
