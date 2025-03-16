from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        cursor = 0
        insert_at = 0

        while cursor < len(chars):
            ch = chars[cursor]
            start = cursor
            while cursor < len(chars) and chars[cursor] == ch:
                cursor += 1
            count = cursor - start

            chars[insert_at] = ch
            insert_at += 1
            if count == 1:
                continue

            for digit in str(count):
                chars[insert_at] = digit
                insert_at += 1

        return insert_at
