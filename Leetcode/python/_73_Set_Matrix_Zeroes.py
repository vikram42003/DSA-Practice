from typing import List


class Solution:
    # Optimal Approach - Time = O(m * n) - Space = O(1)
    # Intuition: We need to remember which rows/cols to zero. To save space, we use the first row and column
    # as our "memory" instead of external arrays.
    #
    # Pitfall: Overwriting the first row/col destroys their original data, which tells us if *they* need to be zeroed.
    # Also, matrix[0][0] is the intersection of both, creating ambiguity.
    #
    # Nuance: We solve this by first checking if the first row/col have zeros and storing that in variables.
    # Then, we use the first row/col to mark the rest of the matrix. We process the inner matrix first using these markers,
    # and finally update the first row/col based on the initial checks.
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])

        # Check first row and col first, before we make any edits to the first row and col in our marking loop
        isThereAnyZeroInFirstRow = any(matrix[0][c] == 0 for c in range(m))
        isThereAnyZeroInFirstCol = any(matrix[r][0] == 0 for r in range(n))

        # Mark rows and columns
        for r in range(1, n):
            for c in range(1, m):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero based on markers
        for r in range(1, n):
            for c in range(1, m):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Zero first row/col if needed
        if isThereAnyZeroInFirstRow:
            for c in range(m):
                matrix[0][c] = 0

        if isThereAnyZeroInFirstCol:
            for r in range(n):
                matrix[r][0] = 0

    # Marker Approach - Time = O(m * n * (m + n)) - Space = O(1)
    # Mark rows/cols with a placeholder (inf) to avoid cascading zeros, then finalize.
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    for i in range(n):
                        matrix[i][c] = float("inf") if matrix[i][c] != 0 else 0
                    for j in range(m):
                        matrix[r][j] = float("inf") if matrix[r][j] != 0 else 0

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == float("inf"):
                    matrix[r][c] = 0
