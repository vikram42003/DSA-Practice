from typing import List


class Solution:
    # Naive - Time = O(n^3) - Space = O(1)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float("inf")
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    sum_ = nums[i] + nums[j] + nums[k]
                    if target - sum_ < closest:
                        closest = target - sum_
                        ans = sum_
                    if closest == target:
                        break

        return ans
