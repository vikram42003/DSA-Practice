class Solution:
    # If n = 2019, then that'll be commas from 1,000 upto 2,019, and whats the total of that? 2021
    # Thus we can just do n - 1000 + 1 only if n > 999
    def countCommas(self, n: int) -> int:
        return n - 1000 + 1 if n > 999 else 0
