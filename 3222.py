"""
3222. Find the Winning Player in Coin Game

You are given two positive integers x and y, denoting the number of coins
with values 75 and 10 respectively.

Alice and Bob are playing a game. Each turn, starting with Alice, the player
must pick up coins with a total value 115. If the player is unable to do so,
they lose the game.

Return the name of the player who wins the game if both players play optimally.
"""


class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        alice = False

        while x > 0 and y > 3:
            x -= 1
            y -= 4
            alice = not alice

        return "Alice" if alice else "Bob"
