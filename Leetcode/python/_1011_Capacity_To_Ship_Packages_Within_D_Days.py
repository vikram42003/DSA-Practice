from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def condition(x: int) -> bool:
            actual_days = 1
            current_load = 0

            for w in weights:
                if current_load + w > x:
                    actual_days += 1
                    current_load = w
                    # Short circuit early if we've already blown past our day limit
                    if actual_days > days:
                        return False
                else:
                    current_load += w
            return True

        # Answer spaces [l,r), based on constraints
        l, r = max(weights), sum(weights)
        while l < r:
            m = l + (r - l) // 2
            if condition(m):
                r = m
            else:
                l = m + 1

        return l
