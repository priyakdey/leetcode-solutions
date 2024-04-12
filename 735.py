"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.
"""

from collections import deque
from typing import Deque, List, cast


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack: Deque[int] = deque()

        for asteroid in asteroids:
            if len(stack) == 0 or asteroid > 0 or stack[-1] < 0:
                stack.append(asteroid)
            else:
                curr = asteroid
                while len(stack) != 0 and stack[-1] > 0 and curr < 0:
                    top = stack.pop()
                    if abs(curr) > abs(top):
                        curr = curr
                    elif abs(curr) < abs(top):
                        curr = top
                    elif abs(curr) == abs(top):
                        curr = 0

                if curr != 0:
                    stack.append(curr)

        return cast(List, stack)
