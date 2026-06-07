import math
from typing import List


class Solution:
    # Binary Search - Time = O(n log n) - Space = O(1)
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # Edge case - If hours is less than len(dist) - 1 (eg. its something like this dist = [1,3,2], hour = 1.9) then its impossible
        # to find a correct ans (since at the very least, we still need 1 time for the trains before the last one)
        if len(dist) - 1 > hour:
            return -1

        def condition(x: int) -> bool:
            timeTaken = 0
            for i in range(len(dist) - 1):
                timeTaken += math.ceil(dist[i] / x)
                if timeTaken > hour:
                    return False
            timeTaken += dist[-1] / x
            return timeTaken <= hour

        l, r = 1, 10**7 + 1
        while l < r:
            m = l + (r - l) // 2
            if condition(m):
                r = m
            else:
                l = m + 1

        return l if condition(l) else -1
