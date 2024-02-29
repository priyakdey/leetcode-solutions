"""
2838. Maximum Coins Heroes Can Collect

There is a battle and n heroes are trying to defeat m monsters. 
You are given two 1-indexed arrays of positive integers heroes and monsters 
of length n and m, respectively. heroes[i] is the power of ith hero, and 
monsters[i] is the power of ith monster.

The ith hero can defeat the jth monster if monsters[j] <= heroes[i].

You are also given a 1-indexed array coins of length m consisting of positive 
integers. coins[i] is the number of coins that each hero earns after defeating 
the ith monster.

Return an array ans of length n where ans[i] is the maximum number of coins 
that the ith hero can collect from this battle.

Notes

The health of a hero doesn't get reduced after defeating a monster.
Multiple heroes can defeat a monster, but each monster can be defeated by a given 
hero only once.
"""

from typing import List, Tuple


class Solution:
    def maximumCoins(
        self, heroes: List[int], monsters: List[int], coins: List[int]
    ) -> List[int]:
        zip_arr = list(zip(monsters, coins))
        zip_arr.sort(key=lambda t: t[0])

        cumm_sum = [zip_arr[0][1] for _ in range(len(zip_arr))]

        for i in range(1, len(zip_arr)):
            cumm_sum[i] = cumm_sum[i - 1] + zip_arr[i][1]

        coins_collected: List[int] = [0 for _ in heroes]
        for i, hero in enumerate(heroes):
            index = self.find_index(zip_arr, hero)
            if index == -1:
                continue
            coins_collected[i] = cumm_sum[index]

        return coins_collected

    def find_index(self, arr: List[Tuple[int, int]], target: int) -> int:
        left, right = 0, len(arr) - 1
        index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] <= target:
                index = mid
                left = mid + 1
            else:
                right = mid - 1

        return index
