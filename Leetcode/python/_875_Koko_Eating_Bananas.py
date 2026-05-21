import math
from typing import List


class Solution:
    # https://www.notion.so/Data-Structures-and-Algorithms-1b89e6c4959d80c28d41c20ba3a209a3?source=copy_link#3679e6c4959d80f8b987f9ca7c26199a
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(k: int) -> bool:
            total = 0
            for p in piles:
                total += math.ceil(p / k)
            return total <= h
    
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
    
    # Binary Search + Check - Time = O(n log n) - Space = O(1)
    # The core idea is that we try different values for k until we find the min val of k
    # that still keeps us within h limit, and then return that val
    # Do be careful with check, we need math.ceil so that if 3/4 still means 1 hour was needed to clear those piles 
    # Also in that l < r + a <= b type of binary search, first condition will be valid window and the ending values
    # of both l and r will be the same and will be the last valid windows
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # l = min time its possible to take
        # r = max time its possible to take, which might just be max elem of piles
        l, r = 1, max(piles)

        if len(piles) == h:
            return r

        while l < r:
            mid = l + ((r - l) // 2)
            hoursTaken = self.check(piles, mid)

            if hoursTaken <= h:
                r = mid
            else:
                l = mid + 1

        return l

    def check(self, piles: List[int], k: int) -> int:
        total = 0
        for p in piles:
            total += math.ceil(p / k)
        return total
