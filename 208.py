from typing import List, Optional


class Node:

    def __init__(self):
        self.children: List[Optional[Node]] = [None] * 26
        self.end = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            index = ord(ch) - ord("a")
            if curr.children[index] is None:
                curr.children[index] = Node()
            curr = curr.children[index]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self._find_node(word)
        if curr is None:
            return False

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, word: str) -> Optional[Node]:
        curr = self.root

        for ch in word:
            index = ord(ch) - ord("a")
            if curr.children[index] is None:
                return None
            curr = curr.children[index]

        return curr
