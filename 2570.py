from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        len1, len2 = len(nums1), len(nums2)
        i, j = 0, 0

        merged: List[List[int]] = []
        while i < len1 and j < len2:
            if nums1[i][0] < nums2[j][0]:
                merged.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                merged.append(nums2[j])
                j += 1
            else:
                value = nums1[i][1] + nums2[j][1]
                merged.append([nums1[i][0], value])
                i += 1
                j += 1

        while i < len1:
            merged.append(nums1[i])
            i += 1

        while j < len2:
            merged.append(nums2[j])
            j += 1

        return merged
