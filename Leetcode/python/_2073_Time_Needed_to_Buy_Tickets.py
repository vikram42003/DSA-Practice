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
