from typing import List


class Solution:
    # Linear Search - Time = O(n^2) - Space = O(1)
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_max = 0
        for account in accounts:
            max_max = max(max_max, sum(account))
        return max_max
