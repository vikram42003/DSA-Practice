from typing import List


class Solution:
    # Greedy - Time = O(n) - Space = O(1)
    # The idea is, if sum(gas) > sum(cost) then an answer WILL exist, and we do greedy to find out
    # where does the consecutive chain of elements where its not unterrupted by uncreachable elements
    #  lies, like where does it start, because then mathematically it WILL be carrying forward the
    # sum we need to cover up the distance till current
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, cur, start = len(gas), 0, 0
        # g and c will sum up gas and cost respectively
        g, c = 0, 0
        for i in range(n):
            diff = gas[i] - cost[i]
            c += cost[i]
            g += gas[i]

            cur += diff
            if cur < 0:
                # i + 1 because on current i, curr is negative, thats why we triggered this condition
                # so i + 1 will be the starting index for the positive subarray segment
                start = i + 1
                cur = 0

        return start if g >= c else -1
