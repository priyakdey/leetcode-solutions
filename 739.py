from collections import deque
from typing import Deque, List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result: List[int] = [0] * len(temperatures)
        stack: Deque[Tuple[int, int]] = deque()

        for curr_day, temperature in enumerate(temperatures):
            while len(stack) > 0 and temperature > stack[-1][0]:
                _, day = stack.pop()
                result[day] = curr_day - day

            stack.append((temperature, curr_day))

        return result
