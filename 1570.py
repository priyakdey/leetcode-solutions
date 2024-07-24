"""
1570. Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class SparseVector:
- SparseVector(nums) Initializes the object with the vector nums
- dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

A sparse vector is a vector that has mostly zero values, you should store the 
sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?
"""

from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.data = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.data[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        if self.length != vec.length:
            raise Exception("vectors are not of same length")

        product = 0
        for i, num in self.data.items():
            if i in vec.data:
                product += num * vec.data[i]

        return product


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
