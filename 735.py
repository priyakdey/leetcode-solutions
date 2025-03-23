from collections import deque
from typing import Deque, List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack: Deque[int] = deque()

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                curr = asteroid
                while len(stack) > 0 and stack[-1] > 0 and curr < 0:
                    top = stack.pop()
                    if abs(curr) > abs(top):
                        curr = curr
                    elif abs(curr) < abs(top):
                        curr = top
                    else:
                        curr = 0

                if curr != 0:
                    stack.append(curr)

        return list(stack)
