from typing import List


class Solution:
    # Naive Solution (Will TLE) - Time = O(n^2) - Space = O(n)
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefixSums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefixSums[i + 1] = prefixSums[i] + nums[i]

        ans = 0
        # i basically says, whats the subarray sum if we start from i in nums, and then include 1 digit after i, then 2 and so on
        # the loop calculates the sum from [0, j) - that means for nums = [-2,5,-1] and i = 0 j = 2, then were getting sum including
        # element 0 and right before element 2 - meaning from 0 to 1
        for i in range(len(nums)):
            # j basically sets the right bound of the window, including the element itself, then 1 another element after it, then the
            # next and so on. Also i starts from i + 1 cause we include an extra 0 to the prefix sum array to make calculations from
            # 0 to j more uniform
            for j in range(i + 1, len(prefixSums)):
                num = prefixSums[j] - prefixSums[i]
                print(num)
                if lower <= num <= upper:
                    ans += 1

        print(prefixSums)
        return -1


test = Solution()
# ans = 3
nums = [-2,5,-1]
lower = -2
upper = 2
print(test.countRangeSum(nums, lower, upper))