class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        prevRow = [0] * (m + 1)
        prevRow[m] = 1

        for i in range(n - 1, -1, -1):
            curRow = prevRow[:]
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    curRow[j] += prevRow[j + 1]
            prevRow = curRow

        return prevRow[0]

    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][m] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]
