"""
443. String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. Note that group lengths that are 
10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the 
array.

You must write an algorithm that uses only constant extra space.
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        last_ch = chars[0]

        insert_at = 0
        curr = 1

        while curr < len(chars):
            if chars[curr] == last_ch:
                count += 1
            else:
                chars[insert_at] = last_ch
                insert_at += 1
                if count != 1:
                    for d in str(count):
                        chars[insert_at] = d
                        insert_at += 1
                last_ch = chars[curr]
                count = 1

            curr += 1

        chars[insert_at] = last_ch
        insert_at += 1
        if count != 1:
            for d in str(count):
                chars[insert_at] = d
                insert_at += 1

        return insert_at
