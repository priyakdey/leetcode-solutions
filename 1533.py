"""
1533. Find the Index of the Large Integer

We have an integer array arr, where all the integers in arr are equal except 
for one integer which is larger than the rest of the integers. You will not be 
given direct access to the array, instead, you will have an API ArrayReader
which have the following functions:

- int compareSub(int l, int r, int x, int y): 
  where 0 <= l, r, x, y < ArrayReader.length(), l <= r and x <= y. 
  The function compares the sum of sub-array arr[l..r] with the sum of the sub-array arr[x..y] and returns:
    - 1 if arr[l]+arr[l+1]+...+arr[r] > arr[x]+arr[x+1]+...+arr[y].
    - 0 if arr[l]+arr[l+1]+...+arr[r] == arr[x]+arr[x+1]+...+arr[y].
    - -1 if arr[l]+arr[l+1]+...+arr[r] < arr[x]+arr[x+1]+...+arr[y].

- int length(): Returns the size of the array.

You are allowed to call compareSub() 20 times at most. You can assume both 
functions work in O(1) time.

Return the index of the array arr which has the largest integer.
"""


class ArrayReader(object):
    """
    This is ArrayReader's API interface.
    You should not implement it, or speculate about its implementation
    """
	
    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
    """
    Compares the sum of arr[l..r] with the sum of arr[x..y]
	return 1 if sum(arr[l..r]) > sum(arr[x..y])
	return 0 if sum(arr[l..r]) == sum(arr[x..y])
	return -1 if sum(arr[l..r]) < sum(arr[x..y])
    """
        pass

    def length(self) -> int:
    """
    Returns the length of the array
    """
        pass

# TODO: Complete this

class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        pass

