from bisect import bisect_left
from typing import List


class Solution:
    # twoPointer the twoSum
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s > target:
                r -= 1
            else:
                l += 1

    # Binary search, kinda not needed tho, can be solved in O(n), and this is O(n log n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for r in range(n - 1, 0, -1):
            needed = target - numbers[r]
            q = bisect_left(numbers, needed, 0, r)

            if q < r and numbers[q] == needed:
                return [q + 1, r + 1]
