from typing import List


class Solution:
    # Dynamic Programming (Fib style recurrence) - Time = O(n) - Space = O(1)
    # If we analyze the problem we see that, If we're at any position curr, then the max amount we can
    # rob would either be curr - 2 + curr([3, 1, 3]), or we can skip curr if curr - 1 > curr - 2 + curr
    # That defines out transition, but for db state, remember we want to track the best cost not just
    # transition states so the dp[curr] should be max(curr - 2 + curr, curr - 1) to store the best possible state so far
    def rob(self, nums: List[int]) -> int:
        prevprev, prev = 0, 0
        # [prevprev, prev, curr, curr + 1, curr + 2, ...]
        for n in nums:
            curr = max(n + prevprev, prev)
            prevprev = prev
            prev = curr
        return prev

    # DFS brute force (TLE) - Time = O(2^n) - Space = O(n)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        maxmax = 0

        def dfs(i):
            nonlocal total, maxmax
            if i >= n:
                return

            total += nums[i]
            maxmax = max(maxmax, total)
            dfs(i + 2)

            total -= nums[i]
            dfs(i + 1)

        dfs(0)
        return maxmax
