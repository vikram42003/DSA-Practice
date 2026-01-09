class Solution:
    # DP (Bottom Up) - Time = O(n * m) - Space = O(n * m)
    # The DP state will be boolean dp[n + 1][m + 1] where n is len(s1) and m is len(s2)
    # Where the presence/absence of chars in s3 from s1 end to current or s2 end to current corelate 
    # to i and j respectively, meaning if dp[0][3] is True that means s3 contains all the chars in s2
    # except the first 2 and no chars from s1. The extra layer we added to n and m will be for if
    # s3 has strings from only s1 or s2
    # If the length of s3 is not equal to n + m then its just False no need to look further
    # We'll set dp[n][m] to True, because it signifies empty string, and s3 will ALWAYS contain empty string
    # Otherwise iterate backwards, check either downwards (which means if i + 1 is true then it means
    # all the chars in s3 uptill now were in s1 or s2) or right (same explanation but for j axis)
    # In the end if the first element was True then thats the answer
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 + n2 != len(s3):
            return False

        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[n1][n2] = True

        for i in range(n1, -1, -1):
            for j in range(n2, -1, -1):
                if i < n1 and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < n2 and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]
