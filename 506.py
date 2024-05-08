"""
506. Relative Ranks

You are given an integer array score of size n, where score[i] is the score of 
the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has 
the highest score, the 2nd place athlete has the 2nd highest score, and so on. 
The placement of each athlete determines their rank:
- The 1st place athlete's rank is "Gold Medal".
- The 2nd place athlete's rank is "Silver Medal".
- The 3rd place athlete's rank is "Bronze Medal".
- For the 4th place to the nth place athlete, their rank is their placement 
  number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = list(map(lambda x: -x, score))
        ranks: List[Tuple[int, int]] = []
        for i, s in enumerate(score):
            heappush(ranks, (s, i))

        answer: List[str] = ["" for _ in score]

        if len(ranks) != 0:
            _, i = heappop(ranks)
            answer[i] = "Gold Medal"

        if len(ranks) != 0:
            _, i = heappop(ranks)
            answer[i] = "Silver Medal"

        if len(ranks) != 0:
            _, i = heappop(ranks)
            answer[i] = "Bronze Medal"

        rank = 4
        while len(ranks) != 0:
            s, i = heappop(ranks)
            answer[i] = str(rank)
            rank += 1

        return answer
