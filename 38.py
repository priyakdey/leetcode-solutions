"""
38. Count and Say

The count-and-say sequence is a sequence of digit strings defined by the 
recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of 
substrings such that each substring contains exactly one unique digit. 
Then for each substring, say the number of digits, then say the digit. 
Finally, concatenate every said digit.
"""

from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.say(self.countAndSay(n - 1))

    def say(self, s: str) -> str:
        count = 1
        digit = s[0]
        buffer: List[str] = []
        for i in range(1, len(s)):
            if s[i] != digit:
                buffer.append(str(count))
                buffer.append(digit)
                digit = s[i]
                count = 0
            count += 1

        buffer.append(str(count))
        buffer.append(digit)
        return "".join(buffer)
