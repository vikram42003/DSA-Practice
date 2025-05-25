from typing import List


class Solution:
    # Brute Force Version - Time = O(n^2) - Space = O(1)
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            j = i + 1
            while j < len(prices) and prices[j] > prices[i]:
                j += 1
            prices[i] -= 0 if j >= len(prices) else prices[j]

        return prices
