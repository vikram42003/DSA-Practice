from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        l, r = 0, len(mat[0]) - 1

        for row in mat:
            if l != r:
                sum += row[l]
                sum += row[r]
            else:
                sum += row[l]
            l += 1
            r -= 1

        return sum
