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

    # Greedy version - Time = O(n) - Space = O(1)
    # What we do is - initially we consider prices[0] as out buy price, since thats the only price we're guarenteed to have
    # And then we iterate over each price and check for
    #   - if the current profit difference is greater than max_profit then update max_profit with that value
    #   - if current price is smaller than our buy price then change buy price to that, since "buy low(est) sell high(est) = $$$"
    # We check for these 2 cases exclusively because if we find a lower value for buy_price, then we'll consider the price difference
    # for the element after the updated buy_price element
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < buy_price:
                buy_price = price
            elif price - buy_price > max_profit:
                max_profit = price - buy_price

        return max_profit
