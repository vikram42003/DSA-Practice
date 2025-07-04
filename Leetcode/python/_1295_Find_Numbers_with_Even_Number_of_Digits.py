from typing import List


class Solution:
    # Basic Linear Search - Time = O(n^2) - Space = O(1)
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            digits = 0
            while n > 0:
                digits += 1
                n //= 10
            if (digits & 1) == 0:
                count += 1
        return count
    
    # Optimized Version - Time = O(n) - Space = O(1)
    # nums[i] can only be 1 to 100000, so just check for number range that has even digits between those bounds 
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if 9 < n < 100 or 999 < n < 10000 or 99999 < n:
                count += 1
        return count 
