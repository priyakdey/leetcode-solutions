class Solution:
    def coloredCells(self, n: int) -> int:
        cells = 1
        for i in range(2, n + 1):
            cells = cells + 4 * (i - 1)

        return cells
