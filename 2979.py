"""
2979. Most Expensive Item That Can Not Be Bought

You are given two distinct prime numbers primeOne and primeTwo.

Alice and Bob are visiting a market. The market has an infinite number of items,
for any positive integer x there exists an item whose price is x. Alice wants to
buy some items from the market to gift to Bob. She has an infinite number of
coins in the denomination primeOne and primeTwo. She wants to know the most
expensive item she can not buy to gift to Bob.

Return the price of the most expensive item which Alice can not gift to Bob.
"""


class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        # chicken mc-nugget problem
        return primeOne * primeTwo - primeOne - primeTwo
