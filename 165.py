"""165. Compare Version Numbers

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. 
Each revision consists of digits and may contain leading zeros. Every revision 
contains at least one character. 
Revisions are 0-indexed from left to right, with the leftmost revision being 
revision 0, the next revision being revision 1, and so on. 
For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. 
Revisions are compared using their integer value ignoring any leading zeros. 
This means that revisions 1 and 001 are considered equal. If a version number 
does not specify a revision at an index, then treat the revision as 0. 
For example, version 1.0 is less than version 1.1 because their revision 0s are 
the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

- If version1 < version2, return -1.
- If version1 > version2, return 1.
- Otherwise, return 0.
"""

from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def atoi(token: str) -> int:
            if token == "":
                return 0
            return int(token)

        def tokenize(version: str) -> List[int]:
            tokens: List[int] = []
            start = 0
            cursor = 0
            while cursor < len(version):
                if version[cursor] == ".":
                    token = atoi(version[start : cursor].strip())
                    tokens.append(token)
                    start = cursor + 1
                cursor += 1

            token = atoi(version[start : cursor].strip())
            if token != 0:
                tokens.append(token)
            return tokens

        def pad(l: List[int], size: int) -> None:
            length = len(l)
            for i in range(length, size):
                l.append(0)

        version1_tokens = tokenize(version1)
        version2_tokens = tokenize(version2)
        size = max(len(version1_tokens), len(version2_tokens))
        pad(version1_tokens, size)
        pad(version2_tokens, size)

        curr = 0
        while curr < size:
            if version1_tokens[curr] < version2_tokens[curr]:
                return -1
            elif version1_tokens[curr] > version2_tokens[curr]:
                return 1
            curr += 1

        return 0

