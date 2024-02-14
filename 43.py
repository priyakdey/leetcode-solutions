"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs 
to integer directly.
"""

from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        product: List[str] = []
        for i in range(len(num2) - 1, -1, -1):
            result = self._multiply(num1, num2[i], len(num2) - 1 - i)
            product = self.add(product, result)

        return "".join(product)

    def add(self, l1: List[str], l2: List[str]) -> List[str]:
        i, j = len(l1) - 1, len(l2) - 1
        carry = 0
        while i >= 0 and j >= 0:
            val = int(l1[i]) + int(l2[j]) + carry
            carry = val // 10
            val = val % 10
            l1[i] = str(val)
            i -= 1
            j -= 1

        while i >= 0:
            val = int(l1[i]) + carry
            carry = val // 10
            val = val % 10
            l1[i] = str(val)
            i -= 1

        while j >= 0:
            val = int(l2[j]) + carry
            carry = val // 10
            val = val % 10
            l1.insert(0, str(val))
            j -= 1

        if carry != 0:
            l1.insert(0, str(carry))

        return l1

    def _multiply(self, num1: str, num2: str, trailing: int) -> List[str]:
        """Returns the product of num1 and num2.
        `trailing` determines the amount of zeros to pad at the end
        """
        num = int(num2)
        product: List[str] = []
        carry = 0
        for i in range(len(num1) - 1, -1, -1):
            val = (int(num1[i]) * num) + carry
            carry = val // 10
            val = val % 10
            product.insert(0, str(val))

        if carry != 0:
            product.insert(0, str(carry))

        for _ in range(trailing):
            product.append("0")

        return product
