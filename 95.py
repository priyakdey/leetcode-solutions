"""

"""

from typing import List, Optional

from model import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_tree(seq: List[int]) -> TreeNode:
            root = TreeNode(seq[0])
            for i in range(1, len(seq)):
                curr, prev = root, None
                while curr is not None:
                    prev = curr
                    if seq[i] < curr.val:
                        curr = curr.left
                    else:
                        curr = curr.right
                if seq[i] < prev.val:
                    prev.left = TreeNode(seq[i])
                else:
                    prev.right = TreeNode(seq[i])

            return root

        def permute(seq: List[int], index: int) -> None:
            nonlocal permutations

            if index == len(seq):
                permutations.append(list(seq))
                return

            permute(seq, index + 1)

            for i in range(index + 1, len(seq)):
                seq[index], seq[i] = seq[i], seq[index]
                permute(seq, index + 1)
                seq[index], seq[i] = seq[i], seq[index]

        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]

        permutations: List[List[int]] = []
        seq: List[int] = [x for x in range(1, n + 1)]
        permute(seq, 0)

        trees: List[TreeNode] = []

        for permutation in permutations:
            trees.append(generate_tree(permutation))

        return trees
