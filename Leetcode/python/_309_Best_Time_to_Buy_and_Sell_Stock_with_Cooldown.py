from typing import List


class Solution:
    # DP (Top Down Memo) - Time = O(n) - Space = O(n)
    def maxProfit(self, prices: List[int]) -> int:
        # For the state, keys will be (idx, buying(boolean)) and value will be the total
        # We'll store the total profit at idx i if we were buying or selling on that day
        memo = {}

        # base case will be out of index, cant do anything with it so return 0, or if the current
        # combination of idx and whether we're buying or selling is already in memo
        # For each index, we can either hold and do nothing regardless of whether we bought or not,
        # or buy if we havent bought, that'll decrease our total, or sell if we have bought already,
        # and that'll increase our total, and then cache whichever branch gives us greater total into
        # the memo
        def rec(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]

            cooldown = rec(i + 1, buying)
            if buying:
                buy = rec(i + 1, False) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
            else:
                sell = rec(i + 2, True) + prices[i]
                memo[(i, buying)] = max(sell, cooldown)

            return memo[(i, buying)]

        return rec(0, True)

    # DFS - Time = O(n^2) - Space = O(n)
    def maxProfit(self, prices: List[int]) -> int:
        def rec(i, buy, total):
            if i >= len(prices):
                return total

            return max(
                (
                    rec(i + 2, -1, total + prices[i] - buy)
                    if buy != -1
                    else rec(i + 1, prices[i], total)
                ),
                rec(i + 1, buy, total),
            )

        return rec(0, -1, 0)
