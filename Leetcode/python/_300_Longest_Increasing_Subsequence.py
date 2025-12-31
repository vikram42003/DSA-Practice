from typing import List


class Solution:
    # DP (Bottom up tabulation) - Time = O(n ^ 2) - Space = O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp states will be the longest increasing substring for each index i
        dp = [1] * n
        max_max = 1

        # then we just pick the longest previously calculated subsequences out of all the
        # subsequences we have calculated, only if the starting point of that substring (nums[j])
        # is greater than the current element (nums[i])
        for i in range(n - 1, -1, -1):
            cur = 0
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    cur = max(cur, dp[j])
            dp[i] += cur
            max_max = max(max_max, dp[i])

        # and return the global max
        return max_max
