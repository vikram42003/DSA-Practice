from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

    def maxProductDifference(self, nums: List[int]) -> int:
        max1, max2, min1, min2 = 0, 0, 10001, 10001
        for n in nums:
            if n >= max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n

            if n <= min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
        return (max1 * max2) - (min1 * min2)
