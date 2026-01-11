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

    # DP (Bottom Up) - Time = O(n * m) - Space = O(n * m)
    # We solve it in a way somewhat similar to 1143. Longest Common Subsequence or 97. Interleaving String
    # The state will be dp[n + 1][m + 1] for tracking the number of ways we can form t[j:] from s[i:] - the dimensions will be len of string s and 
    # t as n and m respectively, plus one extra layer for our base cases
    # the problem states "return the number of distinct subsequences of s which equals t", that means all elements of t should be present in s
    # So the base case includes filling the m'th column with 1 so signify an empty string as t will always be present in s, after that we'll
    # iterate backwards and then take then set dp[i][j] to whats below it (because if s = "bbb" and t = "bb", then due to the duplicating elements
    # both the columns for the first and second b in "bb" will form a part of the column thats consecutively of 1's, denoting the distinct 
    # possibilites, which we should sum up to our final answer) and also add up the diagonal element to dp[i][j] if s[i] == t[j]
    # to get our rolling sum
    # In the end we'll return dp[0][0]
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
