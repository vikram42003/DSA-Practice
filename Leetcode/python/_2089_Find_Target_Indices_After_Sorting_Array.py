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

    # Optimized - Time = O(n) - Space = O(n)
    # Count the elements less than target, and count the number of duplicates of target
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count, less = 0, 0
        for n in nums:
            if n < target:
                less += 1
            elif n == target:
                count += 1

        res = []
        for i in range(count):
            res.append(less)
            less += 1

        return res
