"""
588. Design In-Memory File System

Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

- FileSystem() Initializes the object of the system.
- List<String> ls(String path)
- If path is a file path, returns a list that only contains this file's name.
- If path is a directory path, returns the list of file and directory names 
  in this directory. The answer should in lexicographic order.
- void mkdir(String path) Makes a new directory according to the given path. 
  The given directory path does not exist. If the middle directories in the 
  path do not exist, you should create them as well.
- void addContentToFile(String filePath, String content)
- If filePath does not exist, creates that file containing given content.
- If filePath already exists, appends the given content to original content.
- String readContentFromFile(String filePath) Returns the content in the file 
  at filePath.
"""

from typing import Dict, List, Optional


class File:

    def __init__(self, name: str, content: str = "", is_dir=True):
        self.name = name
        self.is_dir = is_dir
        self.content = content
        self.children: Dict[str, File] = {}


class FileSystem:

    def __init__(self):
        self.root = File("")

    def ls(self, path: str) -> List[str]:
        if path == "/":
            return sorted(self.root.children.keys())

        curr = self.root
        paths = path[1:].split("/")

        for path in paths:
            if path not in curr.children:
                raise Exception("'ls' arguments are invalid: The path doesn't exist")
            curr = curr.children[path]

        if not curr.is_dir:
            return [curr.name]

        return sorted(curr.children.keys())

    def mkdir(self, path: str) -> None:
        curr = self.root
        paths = path[1:].split("/")

        for path in paths:
            if path not in curr.children:
                curr.children[path] = File(path)

            curr = curr.children[path]

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        paths = filePath[1:].split("/")

        for i in range(len(paths) - 1):
            path = paths[i]
            if path not in curr.children:
                raise Exception(
                    "'addContentToFile' arguments are invalid: The path doesn't exist"
                )
            curr = curr.children[path]

        filename = paths[-1]
        if filename not in curr.children:
            curr.children[filename] = File(filename, content, False)
        else:
            curr.children[filename].content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        paths = filePath[1:].split("/")

        for path in paths:
            if path not in curr.children:
                raise Exception(
                    "'addContentToFile' arguments are invalid: The path doesn't exist"
                )
            curr = curr.children[path]
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
