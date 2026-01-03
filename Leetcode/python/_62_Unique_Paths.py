from math import comb


class Solution:
    # Combinatorics (Counting Paths) - Time = O(min(m, n)) - Space = O(1)
    #
    # To reach the bottom-right cell from the top-left:
    # - We must move DOWN exactly (m - 1) times
    # - We must move RIGHT exactly (n - 1) times
    #
    # This means every valid path is a sequence of exactly
    # (m - 1 + n - 1) moves, consisting only of D and R moves.
    #
    # The order of these moves is what makes paths different.
    # Since all Down moves are identical and all Right moves are identical,
    # the problem reduces to choosing which (m - 1) positions
    # (out of m - 1 + n - 1 total positions) will be Down moves.
    #
    # The number of such choices is given by combinations:
    # C(m - 1 + n - 1, m - 1)
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m - 1 + n - 1, m - 1)
    
    # 1D DP (Space Optimized) - Time = O(m * n) - Space = O(n)
    # We can optimize this further, since the state depends on only 1 row and 1 col before cur, we 
    # can just only store 1 row
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]
        return dp[-1]
    
    # 2D DP (Bottom Up Tabulation) - Time = O(n * m) - Space = O(n * m)
    # The state here will be dp[n][m] where its value is the number of ways to reach that nm index
    # Initially, the number of ways to reach any grid[i][j] should be 1, for a gird with a single row
    # or a single column it should be 1 throughout, but as soon as you introduce a second dimension
    # the total number of ways to reach grid[i][j] become the "the number of ways to reach here from
    # top and the number of ways we can reach here from left" (since we can only move right or bottom)
    # Its kind of similar to how throwing two dices have 6 X 6 sample space total, but here since each
    # index depends on the previous index, that becomes our transition
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                top = dp[r - 1][c] if r - 1 >= 0 else 0
                left = dp[r][c - 1] if c - 1 >= 0 else 0
                dp[r][c] = max(top + left, 1)

        print(dp)
        return dp[-1][-1]
