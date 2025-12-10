from typing import List


class Solution:
    # Bottom-Up DP - Time = O(n) - Space = O(n) or O(1)
    # Lets start from the back and iterate backwards, idx n - 1 and n - 2 can directly jump to the
    # top, so the cost from those positions to the top would be their cost itself, so we start
    # from n - 3 idx
    # From here we see, whether we should jump 1 step or 2, by checking whats the minimum. so the
    # cost from this index should be its own cost + whichever next jump has a smaller jump
    # And iterate over the entire list, and since we could start from idx 0 or 1, return the min of the two
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
