"""
224. Basic Calculator

Given a string s representing a valid expression, implement a basic calculator
to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates
strings as mathematical expressions, such as eval().
"""

from collections import deque
from typing import Deque, List


class Solution:
    def calculate(self, s: str) -> int:
        tokens: List[str] = self.tokenize(s)
        print(tokens)

        operands: Deque[str] = deque()
        operators: Deque[str] = deque()

        for token in tokens:
            if token == "(":
                operands.append(token)
            elif token in "+-":
                operators.append(token)
            elif token.isdigit():
                if len(operands) == 0 or operands[-1] == "(":
                    operands.append(token)
                else:
                    op = operators.pop()
                    x = int(operands.pop())
                    y = int(token)
                    if op == "+":
                        operands.append(str(x + y))
                    else:
                        operands.append(str(x - y))
            else:
                y = operands.pop()
                operands.pop()
                if len(operands) == 0 or operands[-1] == "(":
                    operands.append(y)
                else:
                    op = operators.pop()
                    y = int(y)
                    x = int(operands.pop())
                    if op == "+":
                        operands.append(str(x + y))
                    else:
                        operands.append(str(x - y))

        return int(operands[-1])

    def tokenize(self, s: str) -> List[str]:
        tokens: List[str] = []

        curr = 0
        while curr < len(s):
            if s[curr].isspace():
                while curr < len(s) and s[curr].isspace():
                    curr += 1
            elif s[curr] in "()":
                tokens.append(s[curr])
                curr += 1
            elif s[curr] in "+-":
                if len(tokens) == 0 or tokens[-1] == "(":
                    tokens.append("0")
                tokens.append(s[curr])
                curr += 1
            else:
                start = curr
                while curr < len(s) and s[curr].isdigit():
                    curr += 1
                tokens.append(s[start:curr])

        return tokens
