from typing import List


class Solution:
    # Two Pointer - Time = O(n) - Space = O(1)
    # Just do two pointers from left and right, calculate area in between, decrement whichever side is smaller
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        maxWater = 0
        while l < r:
            maxWater = max(maxWater, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxWater
