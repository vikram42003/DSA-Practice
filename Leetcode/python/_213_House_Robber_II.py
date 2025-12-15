from typing import List


class Solution:
    # Case-based DP (Fib style recurrence) - Time = O(2n) = O(n) - Space = O(1)
    # (Check out the comment in lc 198 House Robbers for more details)
    # Houses are connected in a circle. So that means that in the final sum, we can either include the
    # first house or the last house but not both, so how about we search 2 times, one time where we include the house and one time where we dont
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a, b = 0, 0
        for n in range(1, len(nums)):
            cur = max(nums[n] + a, b)
            a = b
            b = cur

        res = b
        a, b = 0, 0
        for n in range(len(nums) - 1):
            cur = max(nums[n] + a, b)
            a = b
            b = cur

        return max(res, b)
