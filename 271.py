"""
271. Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded 
string is then sent over the network and is decoded back to the original 
list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods 
(such as eval).
"""

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""

        buffer: List[str] = ["" for _ in strs]
        cursor = 0

        for s in strs:
            length = len(s)
            buffer[cursor] = str(length) + ":" + s
            cursor += 1

        return "".join(buffer)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        strs: List[str] = []
        cursor = 0

        while cursor < len(s):
            length = 0
            while cursor < len(s) and s[cursor] != ":":
                try:
                    length = length * 10 + int(s[cursor])
                    cursor += 1
                except:
                    raise Exception("bad data format")

            if length < 0 or cursor + length > len(s):
                raise Exception("bad data format")

            cursor = cursor + 1
            strs.append(s[cursor : cursor + length])
            cursor = cursor + length

        return strs
