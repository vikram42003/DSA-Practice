from typing import List


class Solution:
    # Kadane Algo Approach - Time = O(n) - Space = O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        max_max, cur_max = nums[0], 0
        for n in nums:
            if cur_max < 0:
                cur_max = 0
            cur_max += n
            max_max = max(max_max, cur_max)
        return max_max
