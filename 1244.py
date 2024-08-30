"""
1244. Design A Leaderboard

Design a Leaderboard class, which has 3 functions:

- addScore(playerId, score): Update the leaderboard by adding score to the
  given player's score. If there is no player with such id in the leaderboard,
  add him to the leaderboard with the given score.
- top(K): Return the score sum of the top K players.
- reset(playerId): Reset the score of the player with the given id to 0
  (in other words erase it from the leaderboard). It is guaranteed that
  the player was added to the leaderboard before calling this function.

Initially, the leaderboard is empty.
"""

from heapq import heapify, heappop, heappush, heapreplace
from typing import Dict, List


class Player:

    def __init__(self, player_id: int, score: int) -> None:
        self.player_id = player_id
        self.score = score

    def __lt__(self, other: "Player") -> bool:
        return self.score > other.score

    def __str__(self) -> str:
        return f"{self.player_id}: {self.score}"

class Leaderboard:

    def __init__(self):
        self.players: Dict[int, Player] = {}
        self.scoreboard: List[Player] = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.players:
            player = Player(playerId, score)
            self.players[playerId] = player
            heappush(self.scoreboard, player)
        else:
            self.players[playerId].score += score
            heapify(self.scoreboard)

    def top(self, K: int) -> int:
        players: List[Player] = []
        total = 0

        while len(self.scoreboard) > 0 and K > 0:
            player = heappop(self.scoreboard)
            total += player.score
            K -= 1

        for player in players:
            heappush(self.scoreboard, player)

        return total

    def reset(self, playerId: int) -> None:
        player = self.players[playerId]
        self.scoreboard.remove(player)
        del self.players[playerId]
