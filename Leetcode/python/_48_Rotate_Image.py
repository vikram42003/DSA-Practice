from typing import List


class Solution:
    # Transpose + reverse rows - Time = O(n^2) - Space = O(1)
    #
    # A 90° clockwise rotation can be decomposed into two in-place steps
    # First transpose the matrix by swapping (i, j) with (j, i), only traversing
    # half the matrix (j > i) to avoid double swaps
    # Then reverse each row, which shifts elements into their final rotated positions
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i] = matrix[i][::-1]

    # The Cogwheel Technique - Layer-by-layer 4-way rotation - Time = O(n^2) - Space = O(1)
    # Rotate the matrix one layer at a time
    # For each position on the top edge of a layer, rotate the corresponding top bottom left right
    # 4 elements into place using a single temporary variable
    # This moves all elements directly to their final positions without extra memory
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # The cogwheel technique (aptly named by me)
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = matrix[i][j]

                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = temp


# [1,2,3]
# [4,5,6]
# [7,8,9]

# [1,2,3]
# [4,5,6]
# [7,8,9]

# [i,j] -> [j,n-i]

# 00 -> 02

# [0,0] -> [0,2]
# [0,1] -> [1,2]
# [0,2] -> [2,2]

# [1,0] -> [0,1]
# [1,1] -> [1,1]
# [1,2] -> [2,1]

# [2,0] -> [0,0]
# [2,1] -> [1,0]
# [2,2] -> [2,0]
