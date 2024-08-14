"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations: List[str] = []
        self.generate_parenthesis(0, 0, n, [], combinations)
        return combinations

    def generate_parenthesis(
            self, open: int, closed: int, n: int, buffer: List[str],
            combinations: List[str]
    ) -> None:
        if open == closed:
            if open == n:
                combinations.append("".join(buffer))
                return
            else:
                buffer.append("(")
                self.generate_parenthesis(open + 1, closed, n, buffer,
                                          combinations)
                buffer.pop()
        else:
            if open < n:
                buffer.append("(")
                self.generate_parenthesis(open + 1, closed, n, buffer,
                                          combinations)
                buffer.pop()

            buffer.append(")")
            self.generate_parenthesis(open, closed + 1, n, buffer, combinations)
            buffer.pop()
