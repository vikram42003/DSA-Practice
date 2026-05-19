from typing import List


class Solution:
    # Binary Search Binary Search - Time = O(log n * m) - Space = O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while t <= b:
            mid = t + ((b - t) // 2)

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                t = mid + 1
            else:
                b = mid - 1

        row = b
        while l <= r:
            mid = l + ((r - l) // 2)

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
