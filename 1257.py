"""
1257. Smallest Common Region

You are given some lists of regions where the first region of each list
includes all other regions in that list.

Naturally, if a region x contains another region y then x is bigger than y.
Also, by definition, a region x contains itself.

Given two regions: region1 and region2, return the smallest region that
contains both of them.

If you are given regions r1, r2, and r3 such that r1 includes r3, it is
guaranteed there is no r2 such that r2 includes r3.

It is guaranteed the smallest region exists.
"""

from collections import deque
from typing import Deque, Dict, List, Optional


class Solution:
    def findSmallestRegion(
        self, regions: List[List[str]], region1: str, region2: str
    ) -> str:
        tree: Dict[str, Optional[str]] = self.build_tree(regions)
        stack1 = self.parent_stack(tree, region1)
        stack2 = self.parent_stack(tree, region2)

        while stack1[0] != stack2[0]:
            if len(stack1) < len(stack2):
                stack2.pop(0)
            elif len(stack1) == len(stack2):
                stack1.pop(0)
                stack2.pop(0)
            else:
                stack1.pop(0)

        return stack1[0]

    def parent_stack(self, tree: Dict[str, Optional[str]], region: str) -> Deque[str]:
        parents: Deque[str] = deque()

        while region in tree:
            parents.append(region)
            region = tree[region]

        return parents

    def build_tree(self, regions: List[List[str]]) -> Dict[str, str]:
        tree: Dict[str, Optional[str]] = {}
        for parent, *children in regions:
            if parent not in tree:
                tree[parent] = None
            for child in children:
                tree[child] = parent

        return tree


print(Solution().findSmallestRegion([["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]], "Quebec", "New York"))