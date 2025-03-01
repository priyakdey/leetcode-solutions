from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        length = len(pizzas)
        days = length // 4
        odd_days = days // 2 if days & 1 == 0 else days // 2 + 1 
        even_days = days - odd_days 
        
        max_weight: int = 0
        print(pizzas)
        cursor = 0
        for i in range(odd_days):
            print(cursor)
            max_weight += pizzas[cursor]
            cursor += 1

        for i in range(even_days):
            print(cursor)
            max_weight += pizzas[cursor + 1]
            cursor += 2

        return max_weight 

