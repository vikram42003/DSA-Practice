from typing import List


class Solution:
    # The core idea is - we'll be using the calculations of the previous numbers for the current number
    # So this is basically a dp problem
    # For numbers from 0 to 8, you'll see that the number of bits in 4 is just the number of bits
    # in 0 (4 - 4 = 0) + 1, for 5 its number of bits in (5 - 4) + 1, so the transition for the dp is
    # dp[i] = dp[i - offset] + 1, and you'll see that offset grows in exponent of 2s (like for 2 its
    # (2 - 2) + 1, for 4 its (4 - 4) + 1, for 8 its (8 - 8) + 1 and so on)
    # So we'll grow the offset whenever i reaches double of offset
    # and then return dp at the end
    # 0 - 0000
    # 1 - 0001
    # 2 - 0010
    # 3 - 0011
    # 4 - 0100
    # 5 - 0101
    # 6 - 0110
    # 7 - 0111
    # 8 - 1000
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2
            dp[i] = dp[i - offset] + 1
        return dp
