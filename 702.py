# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:


class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 1
        while target > reader.get(right):
            right = right << 1

        while left <= right:
            mid = left + (right - left) // 2
            num = reader.get(mid)
            if target == num:
                return mid
            elif target < num:
                right = mid - 1
            else:
                left = mid + 1

        return -1

