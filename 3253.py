"""
3253. Construct String with Minimum Cost (Easy)

You are given a string target, an array of strings words, and an integer array
costs, both arrays of the same length.

Imagine an empty string s.

You can perform the following operation any number of times (including zero):

Choose an index i in the range [0, words.length - 1].
Append words[i] to s.
The cost of operation is costs[i].
Return the minimum cost to make s equal to target. If it's not possible,
return -1.
"""

from typing import Dict, List, Optional


INT_MAX = (1 << 31) - 1


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        word_dict: Dict[str, int] = {}
        for i in range(len(words)):
            if words[i] in word_dict:
                word_dict[words[i]] = min(costs[i], word_dict[words[i]])
            else:
                word_dict[words[i]] = costs[i]

        length = len(target)
        cache: List[List[Optional[int]]] = [
            [None for _ in range(length + 1)] for _ in range(length + 1)
        ]
        minimum_cost = self.minimum_cost(target, 0, 1, word_dict, cache)
        return minimum_cost if minimum_cost != INT_MAX else -1

    def minimum_cost(
        self,
        target: str,
        start_index: int,
        end_index: int,
        words: Dict[str, int],
        cache: List[List[Optional[int]]],
    ) -> int:
        if end_index == len(target):
            word = target[start_index:end_index]
            if word in words:
                return words[word]
            return INT_MAX

        if cache[start_index][end_index] is not None:
            return cache[start_index][end_index]

        minimum_cost = self.minimum_cost(
            target, start_index, end_index + 1, words, cache
        )

        word = target[start_index:end_index]
        if word in words:
            _cost = self.minimum_cost(target, end_index, end_index + 1, words, cache)
            minimum_cost = min(minimum_cost, words[word] + _cost)

        cache[start_index][end_index] = minimum_cost
        return minimum_cost
