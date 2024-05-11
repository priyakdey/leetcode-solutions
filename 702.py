"""
702. Search in a Sorted Array of Unknown Size

This is an interactive problem.

You have a sorted array of unique elements and an unknown size. You do not 
have an access to the array but you can use the ArrayReader interface to access 
it. You can call ArrayReader.get(i) that:

- returns the value at the ith index (0-indexed) of the secret array 
  (i.e., secret[i]), or
- returns 231 - 1 if the i is out of the boundary of the array.

You are also given an integer target.

Return the index k of the hidden array where secret[k] == target or return -1 
otherwise.

You must write an algorithm with O(log n) runtime complexity.
"""


class ArrayReader:
    """This is ArrayReader's API interface.
    You should not implement it, or speculate about its implementation
    """

    def get(self, index: int) -> int:  # type: ignore
        pass


class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        INT_MAX = (1 << 31) - 1

        left, right = 0, INT_MAX
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            value = reader.get(mid)

            if value == target:
                index = mid
                break
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return index
