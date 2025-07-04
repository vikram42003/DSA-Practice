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
