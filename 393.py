"""
393. UTF-8 Validation

Given an integer array data representing the data, return whether it is a
valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded
characters).

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following
rules:

- For a 1-byte character, the first bit is a 0, followed by its Unicode code.
- For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0,
  followed by n - 1 bytes with the most significant 2 bits being 10

This is how the UTF-8 encoding would work:

     Number of Bytes   |        UTF-8 Octet Sequence
                       |              (binary)
   --------------------+-----------------------------------------
            1          |   0xxxxxxx
            2          |   110xxxxx 10xxxxxx
            3          |   1110xxxx 10xxxxxx 10xxxxxx
            4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

x denotes a bit in the binary form of a byte that may be either 0 or 1.

Note: The input is an array of integers. Only the least significant 8 bits of
each integer is used to store the data. This means each integer represents only
1 byte of data.
"""

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        curr = 0

        while curr < len(data):
            num = data[curr]

            if (num >> 3) & 0x1F == 30:
                length = 4
            elif (num >> 4) & 0xF == 14:
                length = 3
            elif (num >> 5) & 0x7 == 6:
                length = 2
            elif (num >> 7) & 0x1 == 0:
                length = 1
            else:
                return False

            end = curr + length - 1
            while curr < len(data) and curr < end:
                num = data[curr]
                if (num >> 6) & 0x2 != 2:
                    return False
                curr += 1
            curr += 1

        return True
