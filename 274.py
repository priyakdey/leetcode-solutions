"""
274. H-Index

Given an array of integers citations where citations[i] is the number of 
citations a researcher received for their ith paper, return the researcher's 
h-index.

According to the definition of h-index on Wikipedia: 
The h-index is defined as the maximum value of h such that the given researcher 
has published at least h papers that have each been cited at least h times.
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n
        h_index = 0
        while left <= right:
            mid = left + (right - left) // 2
            count = self.count_citations(citations, mid)
            if count >= mid:
                h_index = mid
                left = mid + 1
            else:
                right = mid - 1

        return h_index

    def count_citations(self, citations: List[int], citation: int) -> int:
        count = 0
        for c in citations:
            if c >= citation:
                count += 1

        return count
