from typing import List


class Solution:
    # Sort - Time = O(n log n) - Space = O(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums

    # Two Pointers - Time = O(n) - Space = O(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        res = []
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res.append(nums[i] ** 2)
                i += 1
            else:
                res.append(nums[j] ** 2)
                j -= 1
        return res[::-1]
