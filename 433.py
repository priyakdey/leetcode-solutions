"""
433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices
from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a
gene string endGene where one mutation is defined as one single character
changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations.
A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return
the minimum number of mutations needed to mutate from startGene to endGene.
If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be
included in the bank.
"""
from typing import List


INT_MAX = (1 << 31) - 1


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def generate(buf: List[str], index: int) -> int:
            gene = "".join(buf)
            print(gene)
            if gene == endGene:
                return 0

            if index == len(buf) or gene not in bank:
                return INT_MAX

            steps = generate(buf, index + 1)

            prev_ch = buf[index]

            for ch in "ACGT":
                if prev_ch != ch:
                    buf[index] = ch
                    _steps = generate(buf, index + 1)
                    if _steps != INT_MAX:
                        steps = min(steps, 1 + _steps)

            buf[index] = prev_ch
            return steps

        min_steps = generate(list(startGene), 0)
        return min_steps if min_steps != INT_MAX else -1
