"""
2491. Divide Players Into Teams of Equal Skill

You are given a positive integer array skill of even length n where skill[i]
denotes the skill of the ith player. Divide the players into n / 2 teams of
size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on
that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no
way to divide the players into teams such that the total skill of each team is
equal.
"""

from typing import List


class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        skills.sort()
        left, right = 0, len(skills) - 1
        total = skills[left] + skills[right]
        chemistry = 0
        while left < right:
            if skills[left] + skills[right] != total:
                return -1
            chemistry += skills[left] * skills[right]
            left += 1
            right -= 1

        return chemistry
