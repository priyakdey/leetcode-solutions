"""
216. Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
- Only numbers 1 through 9 are used.
- Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the 
same combination twice, and the combinations may be returned in any order.
"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def generate_combination(curr_value: int, combination: List[int]) -> None:
            nonlocal k, n, combinations

            if len(combination) == k:
                if sum(combination) == n:
                    combinations.append(list(combination))
                return

            if curr_value > 9:
                return

            # go for next value
            generate_combination(curr_value + 1, combination)

            # consider using this current value
            combination.append(curr_value)
            generate_combination(curr_value + 1, combination)
            combination.pop()

        combinations: List[List[int]] = []
        generate_combination(1, [])

        return combinations
