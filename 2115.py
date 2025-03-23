from collections import deque
from typing import Deque, List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        # represents the graph ingredient -> list of recipes
        graph: Dict[str, List[str]] = defaultdict(list)
        # represents the indegree of each recipe
        indegrees: Dict[str, int] = {}

        for i, recipe in enumerate(recipes):
            indegrees[recipe] = len(ingredients[i])

            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)

        # add all supplies to the queue
        queue: Deque[str] = deque()
        for supply in supplies:
            queue.append(supply)

        can_make: List[str] = []

        while len(queue) > 0:
            ingredient = queue.popleft()

            if ingredient not in graph:
                continue

            for recipe in graph[ingredient]:
                indegrees[recipe] -= 1
                if indegrees[recipe] == 0:
                    queue.append(recipe)
                    can_make.append(recipe)

        return can_make
