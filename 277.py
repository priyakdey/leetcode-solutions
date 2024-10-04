"""

"""
from typing import List


# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass

class Solution:
    def findCelebrity(self, n: int) -> int:
        # find all people who do not know anyone

        celebrities: List[int] = []

        for i in range(n):
            is_celebrity = True
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j):
                    is_celebrity = False
                    break
            if is_celebrity:
                celebrities.append(i)

        # go over all the celebrity and see if all others know him
        for celebrity in celebrities:
            is_celebrity = True
            for j in range(n):
                if j == celebrity:
                    continue
                if not knows(j, celebrity):
                    is_celebrity = False
                    break
            if is_celebrity:
                return celebrity

        return -1