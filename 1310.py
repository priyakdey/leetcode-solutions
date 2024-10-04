"""
1310. XOR Queries of a Subarray

You are given an array arr of positive integers. You are also given the array
queries where queries[i] = [left_i, right_i].

For each query i compute the XOR of elements from left_i to right_i
(that is, arr[left_i] XOR arr[left_i + 1] XOR ... XOR arr[right_i] ).

Return an array answer where answer[i] is the answer to the ith query.
"""
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors: List[int] = [0] * (len(arr) + 1)
        for i, num in enumerate(arr):
            xors[i + 1] = xors[i] ^ num

        result: List[int] = []

        for left, right in queries:
            result.append(xors[right + 1] ^ xors[left])

        return result
