from typing import List


class Solution:
    # Bottom-Up DP (Space Optimized) - Time = O(n) - Space = O(1)
    # Using the same intuition of starting from the back, at each step, we can only jump 1 or 2 spots
    # So anything after that is irrelevant to us, we just need to "see" those two spots. So we track
    # those with nxt, nxtnxt, and see from current step, which of these jumps is smaller, and save the
    # result to cur, after we move back nxtnxt will become nxt, and nxt will become cur
    # Do that for each and return whichever of nxt or nxtnxt is smaller (since we can start from 0 or 1 idx)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        nxtnxt = cost[-1]
        nxt = cost[-2]

        i = len(cost) - 3
        while i >= 0:
            cur = min(nxt + cost[i], nxtnxt + cost[i])
            nxtnxt = nxt
            nxt = cur
            i -= 1

        return min(nxt, nxtnxt)

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
