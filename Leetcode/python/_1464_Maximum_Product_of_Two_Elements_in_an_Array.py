from typing import List


class Solution:
    # Simulation - Time = O(n^2) - Space = O(1)
    def maxProduct(self, nums: List[int]) -> int:
        max_max = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                max_max = max(max_max, (nums[i] - 1) * (nums[j] - 1))
        return max_max

    # Sort (Built in Tim Sort) - Time = O(n log n) - Space = O(n)
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)

    # 2 Max - Time = O(n) - Space = O(n)
    def maxProduct(self, nums: List[int]) -> int:
        max1, max2 = 0, 0
        for n in nums:
            if n >= max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n
        return (max1 - 1) * (max2 - 1)
