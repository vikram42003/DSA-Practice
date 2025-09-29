from typing import List


class Solution:
    # Backtrack - Time = O(n * 2 ^ n) - Space = O(n)
    # Same as LC 78. Subsets but we sort the input and skip duplicates at the same level (by checking j > i and nums[j - 1] == nums[j])
    # Sorting is needed since some input could be like [4, 4, 1, 4] and then nums[j - 1] == nums[j] logic will break
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, curr, n = [[]], [], len(nums)
        nums.sort()

        def rec(i):
            for j in range(i, n):
                if j > i and j > 0 and nums[j - 1] == nums[j]:
                    continue
                curr.append(nums[j])
                res.append(curr[:])
                rec(j + 1)
                curr.pop()

        rec(0)

        return res
