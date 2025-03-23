from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def generate(num: int, buf: List[int], index: int, total: int) -> None:
            nonlocal k, n, acc

            if index == k:
                if total == n:
                    acc.append(list(buf))
                return

            if num == 10:
                return

            generate(num + 1, buf, index, total)
            buf[index] = num
            generate(num + 1, buf, index + 1, total + num)

        buf: List[int] = [0] * k
        acc: List[List[int]] = []
        generate(1, buf, 0, 0)
        return acc
