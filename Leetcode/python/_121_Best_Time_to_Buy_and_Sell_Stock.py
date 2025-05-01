from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        i, j = 0, 1
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j += 1
                continue
            
            max_profit = max(prices[j] - prices[i], max_profit)
            j += 1

        return max_profit