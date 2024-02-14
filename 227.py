"""
227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and 
return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. 
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings 
as mathematical expressions, such as eval().
"""

from collections import deque
from typing import Deque


class Solution:
    def calculate(self, s: str) -> int:
        operands_stack: Deque[int] = deque()
        operators_stack: Deque[str] = deque()

        for ch in s:
            match ch:
                case "+" | "-":
                    operators_stack.append(ch)
                case "*":
                    y = operands_stack.pop()
                    x = operands_stack.pop()
                    operands_stack.append(x * y)
                case "/":
                    y = operands_stack.pop()
                    x = operands_stack.pop()
                    if y == 0:
                        raise Exception("cannot divide by zero")
                    operands_stack.append(x // y)
                case _:
                    if not ch.isspace():
                        operands_stack.append(int(ch))

        while len(operators_stack) != 0:
            op = operators_stack.pop()
            y = operands_stack.pop()
            x = operands_stack.pop()
            match op:
                case "+":
                    operands_stack.append(x + y)
                case "-":
                    operands_stack.append(x - y)

        return operands_stack.pop()
