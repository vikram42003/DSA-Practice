class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prevRow = [0] * (len(text2) + 1)

        for r in range(len(text1) - 1, -1, -1):
            curRow = [0] * (len(text2) + 1)
            for c in range(len(text2) - 1, -1, -1):
                if text1[r] == text2[c]:
                    curRow[c] = prevRow[c + 1] + 1
                else:
                    curRow[c] = max(curRow[c + 1], prevRow[c])
            prevRow = curRow

        return prevRow[0]
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n2 + 1)] * (n1 + 1)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
