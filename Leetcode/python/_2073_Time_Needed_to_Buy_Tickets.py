from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        total = 0
        i = 0

        while tickets[k] > 0:
            if tickets[i] == 0:
                i = (i + 1) % n
                continue
            tickets[i] -= 1
            total += 1
            i = (i + 1) % n

        return total

    # Optimized Version
    # Example - tickets = [2,3,2,1] and k = 2
    # Think of it this way - if a person buys all the tickets they need, they're removed from the list right
    # So, for all the people BEFORE k, as far as we're concerned, the longest time they'll spend in the line will be at max k,
    # cause if the value is bigger than k, then by that time k would already be 0 and be out of the list and the question
    # wouldve ended
    # For all the people AFTER k, the longest time for them will be k - 1, cause once k is 0, the problem is solved, we dont care
    # whether have all the tickets they need or not, so we only calculate how much time they'll be spending right before the
    # iteration of the loop where k turns 0
    # check this out for more - https://leetcode.com/problems/time-needed-to-buy-tickets/solutions/4995460/java-easy-solution-beats-100/
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        for i in range(len(tickets)):
            if i <= k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)
        return total
