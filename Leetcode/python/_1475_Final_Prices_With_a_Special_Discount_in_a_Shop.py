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

    # Monotonic Stack Version - Time = O(n + n) = O(n) - Space = O(n)
    # We'll do n operations for array traversal, and another n operations for pushing/popping elements 
    # (since we can only push/pop one element one time only)
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i in range(len(prices) - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()

            disc = stack[-1] if stack else 0
            prices[i] -= disc
            stack.append(prices[i] + disc)

        return prices