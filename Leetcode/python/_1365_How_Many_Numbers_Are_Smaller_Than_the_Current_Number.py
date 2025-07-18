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
    
    # Prefix Sum and Bucket Stuff - Time = O(n) - Space = O(n)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        buckets = [0] * 102
        for i in range(len(nums)):
            buckets[nums[i] + 1] += 1
        
        for i in range(1, 102):
            buckets[i] += buckets[i - 1]

        res = []
        for n in nums:
            res.append(buckets[n])

        return res
