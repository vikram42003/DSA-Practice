from typing import List


class Solution:
    # Simulation - Time = O(n^2) - Space = O(n)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    res[i] += 1
        return res
    
    
