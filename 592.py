"""
592. Fraction Addition and Subtraction

Given a string expression representing an expression of fraction addition and
subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an
integer, change it to the format of a fraction that has a denominator 1.
So in this case, 2 should be converted to 2/1.
"""

from typing import List, Tuple


class Solution:
    def fractionAddition(self, expression: str) -> str:
        tokens = self.tokenize(expression)
        denominator = self.find_lcm(list(map(lambda x: x[1], tokens)))

        numerator = 0
        for x, y in tokens:
            numerator += x * denominator // y

        if numerator == 0:
            return "0/1"

        gcd = self.find_gcd(abs(numerator), denominator)

        return str(numerator // gcd) + "/" + str(denominator // gcd)

    def find_gcd(self, x: int, y: int) -> int:
        if x == 1 or y == 1:
            return 1

        if x < y:
            x, y = y, x

        if y == 0:
            return x

        shift = 0
        while ((x | y) & 1) == 0:
            x = x >> 1
            y = y >> 1
            shift += 1

        while (x & 1) == 0:
            x = x >> 1

        while y != 0:
            while (y & 1) == 0:
                y = y >> 1

            if x > y:
                x, y = y, x

            y = y - x

        return x << shift

    def find_lcm(self, nums: List[int]) -> int:
        lcm = 1
        for num in nums:
            lcm *= num
        return lcm

    def tokenize(self, expression: str) -> List[Tuple[int, int]]:
        tokens: List[Tuple[int, int]] = []
        length = len(expression)
        curr = 0

        while curr < length:
            start = curr
            while curr < length and expression[curr] != "/":
                curr += 1
            numerator = int(expression[start:curr])
            curr += 1
            start = curr
            while curr < length and expression[curr] not in "+-":
                curr += 1
            denominator = int(expression[start:curr])
            tokens.append((numerator, denominator))

        return tokens
