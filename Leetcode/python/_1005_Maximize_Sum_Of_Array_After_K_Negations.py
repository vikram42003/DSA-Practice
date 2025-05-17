from typing import List


class Solution:
    # Greedy - Time = O(n log n) - Space = O(1)
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        nums.sort()
        if k > 0 and k & 1 == 1:
            nums[0] = -nums[0]

        return sum(nums)


test = Solution()
# ans = 22
nums = [-8, 3, -5, -3, -5, -2]
k = 6
print(test.largestSumAfterKNegations(nums, k))
