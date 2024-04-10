"""
60. Permutation Sequence

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following 
sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""

from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        permutations = []
        self.permute(numbers, [], permutations)
        return "".join(map(str, permutations[k - 1]))

    def permute(self, numbers, path, permutations):
        if not numbers:
            permutations.append(path)
        else:
            for i in range(len(numbers)):
                self.permute(
                    numbers[:i] + numbers[i + 1 :], path + [numbers[i]], permutations
                )


# Test the solution
soln = Solution()
print(soln.getPermutation(3, 5))
print(soln.getPermutation(3, 3))
