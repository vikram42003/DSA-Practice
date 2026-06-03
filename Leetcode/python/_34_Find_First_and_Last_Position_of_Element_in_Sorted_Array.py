from typing import List


class Solution:
    # Binary Search - Time = O(log n) - Space = O(1)
    # Standard bisect template, look at notion notes if you're confused
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        leftbound = l

        r = len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1

        rightbound = l - 1

        if (
            0 <= leftbound < len(nums)
            and nums[leftbound] == target
            and 0 <= rightbound < len(nums)
            and nums[rightbound] == target
        ):
            return [leftbound, rightbound]
        else:
            return [-1, -1]
