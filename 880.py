"""
880. Decoded String at Index

You are given an encoded string s. To decode the string to a tape, the encoded 
string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly 
written d - 1 more times in total.

Given an integer k, return the kth letter (1-indexed) in the decoded string.
"""

from typing import List


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        buffer: List[str] = []
        for ch in s:
            if ch in "23456789":
                buffer = buffer * int(ch)
            else:
                buffer.append(ch)

        return buffer[k - 1]


if __name__ == "__main__":
    print(Solution().decodeAtIndex("leet2code3", 10))
    print(Solution().decodeAtIndex("ha22", 5))
    print(Solution().decodeAtIndex("a2345678999999999999999", 1))
