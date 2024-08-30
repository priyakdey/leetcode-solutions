"""
1140. Stone Game II

Alice and Bob continue their games with piles of stones. There are a number of
piles arranged in a row, and each pile has a positive integer number of
stones piles[i].  The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X
remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones
Alice can get.
"""
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        def game(is_alice: bool, index: int, m: int) -> int:
            if index == len(piles):
                return 0
            score = 0
            step = 1

            if is_alice:
                sum = 0
                for i in range(index, min(index + 2 * m , len(piles))):
                    sum += piles[i]
                    score = max(score, sum + game(not is_alice, i + 1, max(step, m)))
                    step += 1
            else:
                step = 1
                for i in range(index, min(index + 2 * m , len(piles))):
                    score = max(score, game(not is_alice, i + 1, max(step, m)))
                    step += 1

            return score

        return game(True, 0, 1)
