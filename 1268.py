from typing import Optional, List


class Node:

    def __init__(self):
        self.children: List[Optional[Node]] = [None] * 26
        self.eow = False


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

        curr.eow = True

    def find_suggestions(self, word: str, start: int, end: int, k: int) -> List[str]:
        curr = self.root
        buf: List[int] = []
        for i in range(start, end):
            ch = word[i]
            index = ord(ch) - ord("a")
            if curr.children[index] is None:
                return []
            buf.append(ch)
            curr = curr.children[index]

        suggestions: List[int] = []
        self.__traverse(curr, buf, suggestions, k)
        return suggestions

    def __traverse(
        self, node: Node, buf: List[str], suggestions: List[str], k: int
    ) -> None:
        if len(suggestions) == k:
            return

        if node.eow:
            suggestions.append("".join(buf))

        for i in range(26):
            child = node.children[i]
            if child is not None:
                buf.append(chr(i + ord("a")))
                self.__traverse(child, buf, suggestions, k)
                buf.pop()


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie: Trie = Trie()
        for product in products:
            trie.insert(product)

        suggestions: List[List[str]] = []

        for i in range(len(searchWord)):
            suggestions.append(trie.find_suggestions(searchWord, 0, i + 1, 3))

        return suggestions
