from typing import List


class Solution:
    def finalString(self, s: str) -> str:
        def reverse(buf: List[str]) -> None:
            left, right = 0, len(buf) - 1

            while left < right:
                buf[left], buf[right] = buf[right], buf[left]
                left += 1
                right -= 1

        buf: List[str] = []
        for ch in s:
            if ch == "i":
                reverse(buf)
            else:
                buf.append(ch)

        return "".join(buf)
