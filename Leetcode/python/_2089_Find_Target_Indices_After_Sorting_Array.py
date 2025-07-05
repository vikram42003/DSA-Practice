from typing import List


class Solution:
    # Sort and Linear Search - Time = O(n log n) - Space = O(n)
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n == target:
                res.append(i)

        return res

    # Oneline Version (Bit slower for some reason)
    # Sort and Linear Search - Time = O(n log n) - Space = O(n)
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i in range(len(nums)) if nums[i] == target]
