from typing import List


class Solution:
    # Sliding Window - Time = O(n) - Space = O(1)
    def longestOnes(self, nums: List[int], k: int) -> int:
        cur = 0
        max_max = 0
        zeroCount = 0
        l = 0

        for r in range(len(nums)):
            cur += 1

            if nums[r] == 0:
                zeroCount += 1

            while l < len(nums) and zeroCount > k:
                cur -= 1
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1

            max_max = max(max_max, cur)

        return max_max
