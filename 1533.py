# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: "ArrayReader") -> int:
        left, right = 0, reader.length() - 1

        index = -1

        while left <= right:
            slice_length = right - left + 1
            mid = left + (right - left) // 2

            if slice_length & 1 == 0:
                compare_sub = reader.compareSub(left, mid, mid + 1, right)
                if compare_sub == 1:
                    right = mid
                elif compare_sub == -1:
                    left = mid + 1
                else:
                    # should never hit this if slice length is even
                    raise Exception("something went wrong")
            else:
                if left == right:
                    index = mid
                    break
                compare_sub = reader.compareSub(left, mid - 1, mid + 1, right)
                if compare_sub == 1:
                    right = mid - 1
                elif compare_sub == -1:
                    left = mid + 1
                else:
                    index = mid
                    break

        return index

