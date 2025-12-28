class Solution:
    # DP (Bottom-Up, Space Optimized) - Time = O(n), Space = O(1)
    # dp[i] = number of ways to decode substring s[i:]
    # From each index, we see how many total ways would we have of getting there, we can take 1 digit or 2 digits (if valid),
    # so dp[i] = dp[i+1] + dp[i+2] when allowed.
    # We iterate backwards and keep only the last two states.
    def numDecodings(self, s: str) -> int:
        n = len(s)
        nxt, nxtnxt = 1, 0

        for i in range(n - 1, -1, -1):
            curr = 0
            if s[i] != "0":
                curr = nxt
                if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                    curr += nxtnxt
            nxtnxt, nxt = nxt, curr

        return nxt
