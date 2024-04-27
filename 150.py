"""
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic 
expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

from collections import deque
from typing import Deque, List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]

        stack: Deque[int] = deque()

        for token in tokens:
            if token in ops:
                op2, op1 = stack.pop(), stack.pop()
                result = self.eval(op1, op2, token)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()

    def eval(self, lhs: int, rhs: int, op: str) -> int:
        match op:
            case "+":
                return lhs + rhs
            case "-":
                return lhs - rhs
            case "*":
                return lhs * rhs
            case "/":
                return int(lhs / rhs)
            case _:
                raise Exception("Invalid operator")
