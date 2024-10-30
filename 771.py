"""
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a
type of stone you have. You want to know how many of the stones you have are
also jewels.

Letters are case sensitive, so "a" is considered a different type of stone
from "A".
"""
from typing import Set


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        distinct: Set[str] = set(jewels)
        jewel_count: int = 0

        for stone in stones:
            if stone in distinct:
                jewel_count += 1

        return jewel_count