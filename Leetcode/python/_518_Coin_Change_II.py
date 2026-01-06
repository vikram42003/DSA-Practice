from typing import List


class Solution:
    # DP (Bottom Up Tabulation) - Time = O(n * amount) - Space = O(amount)
    # Since we're building bottom up, the states will be the number of ways we can make amount a for any a from 0 to amount
    # We can always make amount 0, so set that as 1 as the base case, and then for each coin try to make every amount,
    # The ways to make amount a would be the ways to make a - coin amount added to the ways to make the current amount we have
    # already calculated. Eg for a as 1 and coin as 1, dp[a] += dp[a - coin] which is dp[1] += dp[1 - 1], so 1 way of making 
    # amount 1 if we have a coin of 1, same for 2, and then when we get to coin 2 and starting amt 2, we'll do dp[2] += dp[2 - 2]
    # then dp[2] will have its final value as 2 so far, and so on for more amounts and coins
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]

    # DP (Top Down Memo) - Time = O(n * amount) - Space = O(n * amount + n)
    # Similar to dfs except we return a value in the rec function and cache the results in memo
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def rec(i, cur):
            if i >= len(coins) or cur < 0:
                return 0
            if cur == 0:
                return 1
            if (i, cur) in memo:
                return memo[(i, cur)]

            memo[(i, cur)] = rec(i, cur - coins[i]) + rec(i + 1, cur)
            return memo[(i, cur)]

        return rec(0, amount)

    # DFS - Time = O(n ^ 2) - Space = O(n)
    # For each coin we can either take it again, or just move to next coin from here
    # (the take current coin and move forward route will automatically be covered by when we do take in current
    # iteration and then move forward and enter the skip route in the second iteration)
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0

        def rec(i, cur):
            if i >= len(coins) or cur < 0:
                return
            if cur == 0:
                nonlocal res
                res += 1
                return

            rec(i, cur - coins[i])
            rec(i + 1, cur)

        rec(0, amount)
        return res
