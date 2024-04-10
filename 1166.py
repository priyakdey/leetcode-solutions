"""
1166. Design File System

You are asked to design a file system that allows you to create new paths and 
associate them with different values.

The format of a path is one or more concatenated strings of the form: 
/ followed by one or more lowercase English letters. 
For example, "/leetcode" and "/leetcode/problems" are valid paths while an 
empty string "" and "/" are not.

Implement the FileSystem class:

- bool createPath(string path, int value) Creates a new path and associates a 
  value to it if possible and returns true. Returns false if the path already 
  exists or its parent path doesn't exist.
- int get(string path) Returns the value associated with path or 
  returns -1 if the path doesn't exist.
"""

from typing import Dict, List


class Node:
    def __init__(self, path="/", value=0):
        self.path = path
        self.children: Dict[str, Node] = {}
        self.value = value


class FileSystem:
    def __init__(self):
        self.root = Node()

    def createPath(self, path: str, value: int) -> bool:
        if path == "/" or path == "":
            return False

        paths: List[str] = path.split("/")
        paths = paths[1:]

        curr = self.root

        cursor = 0
        while cursor < len(paths) - 1:
            p = paths[cursor]
            if p not in curr.children:
                return False
            curr = curr.children[p]
            cursor += 1

        if paths[-1] in curr.children:
            return False

        curr.children[paths[-1]] = Node(paths[-1], value)
        return True

    def get(self, path: str) -> int:
        curr = self.root
        paths: List[str] = path.split("/")
        paths = paths[1:]

        for path in paths:
            if path not in curr.children:
                return -1
            curr = curr.children[path]

        return curr.value
