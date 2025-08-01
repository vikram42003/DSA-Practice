from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if left < i:
                nums[left], nums[i] = nums[i], nums[left]
            left += 1
