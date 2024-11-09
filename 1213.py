"""
1213. Intersection of Three Sorted Arrays

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing
order, return a sorted array of only the integers that appeared in all three
arrays.
"""

import typing
from typing import List


class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        distinct2: typing.Set[int] = set(arr2)
        distinct3: typing.Set[int] = set(arr3)

        common_elements: List[int] = []

        for num in arr1:
            if num in distinct2 and num in distinct3:
                common_elements.append(num)

        return common_elements
