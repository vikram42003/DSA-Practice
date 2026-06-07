from typing import List


class Solution:
    # Binary search - Time = O(n log n) - Space = O(1)
    # The usual bisect binary search template
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def condition(x: int) -> bool:
            cur = 0
            for t in time:
                cur += x // t
                if cur >= totalTrips:
                    return True
            return False

        l, r = 1, min(time) * totalTrips + 1
        while l < r:
            m = l + (r - l) // 2
            if condition(m):
                r = m
            else:
                l = m + 1

        return l
