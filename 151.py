from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        buf: List[str] = []
        cursor = len(s) - 1
        while cursor >= 0:
            if s[cursor] == " ":
                cursor -= 1
            else:
                end = cursor
                while cursor >= 0 and s[cursor] != " ":
                    cursor -= 1
                buf.append(s[cursor + 1 : end + 1])

        return " ".join(buf)
