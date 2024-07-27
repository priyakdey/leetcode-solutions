"""
2976. Minimum Cost to Convert String I

You are given two 0-indexed strings source and target, both of length n and
consisting of lowercase English letters. You are also given two 0-indexed
character arrays original and changed, and an integer array cost, where cost[i]
represents the cost of changing the character original[i] to the character
changed[i].

You start with the string source. In one operation, you can pick a character
x from the string and change it to the character y at a cost of z if there
exists any index j such that cost[j] == z, original[j] == x, and
changed[j] == y.

Return the minimum cost to convert the string source to the string target
using any number of operations. If it is impossible to convert source to
target, return -1.

Note that there may exist indices i, j such that original[j] == original[i]
and changed[j] == changed[i].
"""
from typing import List, Tuple, Dict


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str],
                    changed: List[str], cost: List[int]) -> int:
        cost_mapping: Dict[Tuple[str, str], int] = {}
        for i in range(len(original)):
            cost_mapping[(original[i], changed[i])] = cost[i]

        min_cost = 0
        for i, ch in enumerate(source):
            key: Tuple[str, str] = ch, target[i]
            if key not in cost_mapping:
                return -1
            min_cost += cost_mapping[key]

        return min_cost
