from typing import List


class Solution:
    # Brute Force Solution - Time = O(n^2) - Space = O(1)
    def countKDifference(self, nums: List[int], k: int) -> int:
        total = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    total += 1

        return total
    
    # HashMap Approach - Time = O(n) - Space = O(n)
    def countKDifference(self, nums: List[int], k: int) -> int:
        total = 0
        hashmap = {}

        for num in nums:
            if num - k in hashmap:
                total += hashmap[num - k]
            if num + k in hashmap:
                total += hashmap[num + k]
            hashmap[num] = hashmap.get(num, 0) + 1

        return total