from typing import List


class Solution:
    # Kadane - Time = O(n) - Space = O(1)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_max = 0
        for i in nums:
            if i == 1:
                count += 1
                max_max = max(max_max, count)
            else:
                count = 0
        return max_max
