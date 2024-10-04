"""
1605. Find Valid Matrix Given Row and Column Sums

You are given two arrays rowSum and colSum of non-negative integers where
rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum
of the elements of the jth column of a 2D matrix. In other words, you do not
know the elements of the matrix, but you do know the sums of each row and
column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length
that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements.
It's guaranteed that at least one matrix that fulfills the requirements exists.
"""

from heapq import heapify, heappop
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)

        row_sums = [(row_sum, row) for row, row_sum in enumerate(rowSum)]
        col_sums = [(col_sum, col) for col, col_sum in enumerate(colSum)]
        heapify(row_sums)
        heapify(col_sums)

        matrix: List[List[int]] = [[-1 for _ in range(cols)] for _ in range(rows)]

        curr_row_sums: List[int] = [0] * rows
        curr_col_sums: List[int] = [0] * cols

        for i in range(rows * cols):
            if len(row_sums) == 0:
                col_sum, col = heappop(col_sums)
                curr_col_sum = curr_col_sums[col]
                value = col_sum - curr_col_sum
                row = 0
                while row < rows:
                    if matrix[row][col] == -1:
                        matrix[row][col] = value
                        break
                    row += 1
                curr_col_sums[col] += value
                curr_row_sums[row] += value
            elif len(col_sums) == 0:
                row_sum, row = heappop(row_sums)
                curr_row_sum = curr_row_sums[row]
                value = row_sum - curr_row_sum
                col = 0
                while col < cols:
                    if matrix[row][col] == -1:
                        matrix[row][col] = value
                        break
                    col += 1
                curr_row_sums[row] += value
                curr_col_sums[col] += value
            elif row_sums[0][0] <= col_sums[0][0]:
                row_sum, row = heappop(row_sums)
                curr_row_sum = curr_row_sums[row]
                value = row_sum - curr_row_sum
                col = 0
                while col < cols:
                    if matrix[row][col] == -1:
                        matrix[row][col] = value
                        break
                    col += 1
                curr_row_sums[row] += value
                curr_col_sums[col] += value
            else:
                col_sum, col = heappop(col_sums)
                curr_col_sum = curr_col_sums[col]
                value = col_sum - curr_col_sum
                row = 0
                while row < rows:
                    if matrix[row][col] == -1:
                        matrix[row][col] = value
                        break
                    row += 1
                curr_col_sums[col] += value
                curr_row_sums[row] += value
        return matrix
