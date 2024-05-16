"""
275. H-Index II

Given an array of integers citations where citations[i] is the number of 
citations a researcher received for their ith paper and citations is sorted 
in ascending order, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as 
the maximum value of h such that the given researcher has published at least 
h papers that have each been cited at least h times.

You must write an algorithm that runs in logarithmic time.
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        left, right = 0, len(citations)

        while left <= right:
            mid = left + (right - left) // 2
            count = self.min_paper_with_citation_count(citations, mid)
            if count >= mid:
                h_index = mid
                left = mid + 1
            else:
                right = mid - 1

        return h_index

    def min_paper_with_citation_count(self, citations: List[int], citation: int) -> int:
        left, right = 0, len(citations) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] >= citation:
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        if index == -1:
            return 0

        return len(citations) - 1 - index + 1
