"""
71. Simplify Path

Given an absolute path for a Unix-style file system, which begins with a slash
'/', transform this path into its simplified canonical path.

In Unix-style file system context, a single period '.' signifies the current
directory, a double period ".." denotes moving up one directory level, and
multiple slashes such as "//" are interpreted as a single slash. In this
problem, treat sequences of periods not covered by the previous rules
(like "...") as valid names for files or directories.

The simplified canonical path should adhere to the following rules:

- It must start with a single slash '/'.
- Directories within the path should be separated by only one slash '/'.
- It should not end with a slash '/', unless it's the root directory.
- It should exclude any single or double periods used to denote current or
  parent directories.

Return the new path.
"""
from collections import deque
from typing import Deque, List


class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = self.tokenize(path)

        stack: Deque[str] = deque()

        for token in tokens:
            if token == '..':
                if len(stack) != 0:
                    stack.pop()
            elif token == ".":
                continue
            else:
                stack.append(token)

        return "/" + "/".join(stack)

    def tokenize(self, path: str) -> List[str]:
        tokens: List[str] = []

        curr = 0
        while curr < len(path):
            # skip all slashes
            while curr < len(path) and path[curr] == "/":
                curr += 1
            start = curr
            while curr < len(path) and path[curr] != "/":
                curr += 1

            token = path[start:curr]
            if len(token) != 0:
                tokens.append(token)

        return tokens
