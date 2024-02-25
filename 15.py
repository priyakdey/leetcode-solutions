"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

"""

from typing import List, Set


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cache: Set[int] = set()

        def find_pair_for_number(start: int, num: int) -> List[List[int]]:
            """This function is a memoization for def _find_pair_for_number. This
            should be used for performance and neglecting duplicates.

            @Note: Could have also done how to skipped duplicates in _find_pair_for_number,
            that would save space in terms of cache. But this is because I have a ref
            back to how memoization works - a fancy term for a function cache !!
            """
            triplets: List[List[int]] = []
            if num not in cache:
                triplets = _find_pair_for_number(start, num)
                cache.add(num)

            return triplets

        def _find_pair_for_number(start: int, num: int) -> List[List[int]]:
            """Function to find triplet pairs from start index to end
            for which num + nums[i] + num[j] == 0. This function to find
            all unique and satisfying i and j for num.
            """
            triplets: List[List[int]] = []
            end = len(nums) - 1
            _start = start
            while start < end:
                if start > _start and nums[start] == nums[start - 1]:
                    # this will avoid duplicate triplets
                    start += 1
                    continue
                total = num + nums[start] + nums[end]
                if total == 0:
                    triplets.append([num, nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1

            return triplets

        nums.sort()
        triplets: List[List[int]] = []
        for i in range(0, len(nums) - 3 + 1):
            triplets.extend(find_pair_for_number(i + 1, nums[i]))

        return triplets
