from typing import List


class Solution:
    # Bound Based + Target Based Binary Search - Time - O(log n + log m) = O(log m * n) - Space = O(1)
    # First do a bound based binary search looking for first time matrix[m][0] > target and then do the classic target based binary search
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m

        while l < r:
            m = l + (r - l) // 2
            if target < matrix[m][0]:
                r = m
            else:
                l = m + 1
        
        row = l - 1
        
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False
    
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
