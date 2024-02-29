"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers 
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen 
numbers is different.

The test cases are generated such that the number of unique combinations that 
sum up to target is less than 150 combinations for the given input.
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combination(index: int, curr_sum: int, buffer: List[int]) -> None:
            nonlocal candidates
            nonlocal target
            nonlocal combinations

            if curr_sum == target:
                l = list(buffer)
                if l not in combinations:
                    combinations.append(l)
                return

            if curr_sum > target or index == len(candidates):
                return

            combination(index + 1, curr_sum, buffer)

            for i in range(index, len(candidates)):
                buffer.append(candidates[index])
                combination(i, curr_sum + candidates[index], buffer)
                buffer.pop()

        combinations: List[List[int]] = []
        combination(0, 0, [])
        return combinations
