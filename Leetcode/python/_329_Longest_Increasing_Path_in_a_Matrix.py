from typing import List


class Solution:
    # DP (Top Dowm Memo) - Time = O(n * m) - Space = O(n * m)
    # As a human, how would i solve this problem. Its pretty intuitive right, look at each element in the grid
    # count how many elements long of a sequence i see, and then track whats the largest one I saw.
    # This is just that but memo'd, we take a look at every single element, look at all 4 directions and recursively keep looking
    # And the we memo it by tracking what was the longest sequence we saw at this element, cache it in memo, and return its val
    # If we go out of bounds then its invalid so return 0, each element itself would form a sequence of 1 length, and every
    # time out check condition evaluates to true, then add 1 to whatever result a recursive call would've returned to account
    # for the found valid element
    # Since we know the dimensions, we can just use a n * m grid instead of a dict memo
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        dp = [[0] * m for _ in range(n)]

        def rec(r, c):
            if dp[r][c] != 0:
                return dp[r][c]

            dp[r][c] = 1
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and matrix[r][c] < matrix[nr][nc]:
                    dp[r][c] = max(dp[r][c], 1 + rec(nr, nc))
            return dp[r][c]

        res = 0
        for r in range(n):
            for c in range(m):
                res = max(res, rec(r, c))

        return res
    
    # DFS - Time = O(4 ^ (n * m)) - Space = O(n * m)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def rec(r, c):
            if not (0 <= r < n) or not (0 <= c < m):
                return 0

            cur = 1
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and matrix[r][c] < matrix[nr][nc]:
                    cur = max(cur, rec(nr, nc) + 1)
            return cur

        res = 0
        for r in range(n):
            for c in range(m):
                res = max(res, rec(r, c))
        
        return res
