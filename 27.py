"""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of 
val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to 
get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the 
  elements which are not equal to val. The remaining elements of nums are not 
  important as well as the size of nums.
- Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None:
            raise Exception("invalid input")

        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return 1 if nums[0] != val else 0

        left, right = 0, length - 1
        while left < right:
            if nums[left] == val and nums[right] == val:
                right -= 1
            elif nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] != val and nums[right] == val:
                left += 1
                right -= 1
            elif nums[left] != val and nums[right] != val:
                left += 1

        if nums[left] == val:
            return left
        else:
            return left + 1
