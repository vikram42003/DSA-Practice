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

    # Divide and Conquer - Time = O(n log n) - Space = O(log n)
    # prefix for right half and suffix for left half, expand from center, sum until boundaries, and
    # recursively do the same inside each half (first), then take the global max
    def maxSubArray(self, nums: List[int]) -> int:
        def rec(l, r):
            if l >= r:
                return nums[l]

            mid = l + ((r - l) // 2)
            left_local_max = rec(l, mid)
            right_local_max = rec(mid + 1, r)

            l_cur = 0
            l_max = float("-inf")
            for i in range(mid, l - 1, -1):
                l_cur += nums[i]
                l_max = max(l_max, l_cur)

            r_cur = 0
            r_max = float("-inf")
            for j in range(mid + 1, r + 1):
                r_cur += nums[j]
                r_max = max(r_max, r_cur)

            cur_max = l_max + r_max
            return max(cur_max, left_local_max, right_local_max)

        return rec(0, len(nums) - 1)
