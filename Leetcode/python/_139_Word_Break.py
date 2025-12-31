from typing import List


class Solution:
    # DP (Bottom Up tabs) - Time = O(n * m * k) - Space = O(n)
    # The core idea is, we start from the end and for each position we check if
    # there is any word in wordDict that can get us from current pos to the end (denoted by dp[i] being true)
    # So the state would be the length of the word + 1 for denoting we have reached the end, and set each idx to False
    # except last idx which is True
    # Now for each word in wordDict, first check if the length curr to end is greater than or equal to the word (to ensure
    # we dont go out of bounds), then check if the substring matches. If yes, then update dp[i] using dp[i + len(word)]
    # and immediately break if a True is found, to ensure we dont overwrite a correct path
    # In the end just return whats in dp[0], its bool value will tell us whether any sequence of jumps made us reach the end
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                wn = len(w)
                if n - i >= wn and s[i : i + wn] == w:
                    dp[i] = dp[i + wn]
                if dp[i]:
                    break

        return dp[0]
