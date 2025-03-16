from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = 0, 0
        banned_radiant, banned_dire = 0, 0
        queue = deque()
        for senator in senate:
            queue.append(senator)
            if senator == "R":
                radiant += 1
            else:
                dire += 1

        while len(queue) > 0 and radiant > 0 and dire > 0:
            senator = queue.popleft()

            # first we check if need to ban this senator
            if senator == "R" and banned_radiant > 0:
                banned_radiant -= 1
                radiant -= 1
                continue
            if senator == "D" and banned_dire > 0:
                banned_dire -= 1
                dire -= 1
                continue

            if senator == "R":
                banned_dire += 1
            else:
                banned_radiant += 1
            queue.append(senator)

        return "Radiant" if radiant > 0 else "Dire"
