class Solution:
    # DP (Bottom Up) - Time = O(n * m) - Space = O(n * m)
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        # An empty string should match an empty pattern base case
        dp[n][m] = True

        # We iterate upto n, because the nth row represents an empty string, and we also have to
        # consider that
        for i in range(n, -1, -1):
            for j in range(m - 1, -1, -1):
                match = i < n and (s[i] == p[j] or p[j] == ".")
                if j + 1 < m and p[j + 1] == "*":
                    dp[i][j] = (match and dp[i + 1][j]) or dp[i][j + 2]
                elif match:
                    dp[i][j] = dp[i + 1][j + 1]

        return dp[0][0]
    
    # DP (Top Down) - Time = O(n * m) - Space = O(n * m)
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = {}

        def rec(i, j):
            # If both i and j make it to the end then its a true
            if i == n and j == m:
                return True
            # If we've exhausted the pattern then return false
            # (also if we've exhausted i then it doesnt necessarily mean its a mathc because s could be "" and p could be "a"
            # so it wont match then)
            if j == m:
                return False

            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = False
            match = i < n and (s[i] == p[j] or p[j] == ".")
            # Asterisk case
            if j + 1 < m and p[j + 1] == "*":
                # Do the repeat current element or not repeate current branching
                # If the first characters match then only move i and repeat j
                # Otherwise skip the j'th and the "*" elements
                dp[(i, j)] = (match and rec(i + 1, j)) or rec(i, j + 2)
            # If both strings are equal or p[j] == "." then move both i and j
            elif match:
                dp[(i, j)] = rec(i + 1, j + 1)

            return dp[(i, j)]

        return rec(0, 0)
