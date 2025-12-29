from typing import List


class Solution:
    # DP (Bottom up and tabulation) - Time = O() - Space = O(n)
    # Initialize the tabulation dp with a base value, lets take it as amount + 1, because that will
    # be the first impossible value since the array will be of size amount + 1, cause we'll add a
    # 0 as a base case

    # now iterate from 1 to amount (inclusive) and then build up the solution, like first see how
    # many coins we need for 1, that will just be 1 coin, only if the array has 1, then look at 2,
    # how many coins do we need for 2, for that we'll iterate over the coins, and do 1 + 
    # dp[amt - curr_coin_val], 1 to pick the current coin and then after pickign that coin the
    # remaining value would be lesser and something we have already calculated so we can just 
    # use that. And we'll assign dp[amt] with the min value, by doing dp[amt] = min(dp[amt], 
    # dp[amt - c]), so that we only store the min value and dont overwrite with a larger val

    # then return dp[amount] only if its not set to our base value, representing that there is a
    # valid combination
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
    
    # Backtracking - Time O(n^3) - Space = O(n)
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)

        def backtrack(i, amt):
            if amt == 0:
                return 0
            if amt < 0 or i < 0:
                return float("inf")
            
            take_reuse = 1 + backtrack(i, amt - coins[i])
            take_move = 1 + backtrack(i - 1, amt - coins[i])
            move = backtrack(i - 1, amt)

            return min(take_reuse, take_move, move)
        
        ans = backtrack(n - 1, amount)
        return ans if ans != float('inf') else -1

    # Greedy (Wont work here) - Time O(n log n) - Space = O(n)
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        total, n = 0, len(coins)
        for i in range(n - 1, -1, -1):
            total += amount // coins[i]
            amount = amount % coins[i]
            if amount == 0:
                break
        return total if amount == 0 else -1