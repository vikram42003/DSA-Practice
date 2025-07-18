from typing import List


class Solution:
    # Simulation - Time = O(n^2) - Space = O(1)
    def maxProduct(self, nums: List[int]) -> int:
        max_max = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                max_max = max(max_max, (nums[i] - 1) * (nums[j] - 1))
        return max_max
    
    
