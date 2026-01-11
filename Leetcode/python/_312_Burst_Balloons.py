from typing import List


class Solution:
    # DP (Top Down) - Time = O(n ^ 3) - Space = O(n ^ 2)
    # <MEMORIZE THIS ONE> Its a super hard one and very non intuitive, link - https://www.youtube.com/watch?v=VFskby7lUbw
    # The main idea we follow is - lets add the boundary elements of 1 to the array and how about
    # thinking that our boundaries are l and r at new array called ballons idx 1 and len(ballon) - 2,
    # and lets think that for each idx i between (including both) l and r, we pop that i index last
    # Then in that calculation current element will just be balloons[l - 1] * balloons[i] * balloons
    # [r + 1] + the coins we'll be able to make from the left subarray whose boundaries will be
    # (l, i - 1) + the right subarray whose boundaries will be (i + 1, r)
    # In that way we will correctly be able to include the current element in the calculations for
    # elements which are to the immediate left and right of i, and the l and r indices will give us
    # something to cache in the dp.
    # So just do it like that, in a recursive function and return the result
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        dp = {}

        def rec(l, r):
            # If left has passed right then just return 0, we've computed all subarrrays from this side
            if l > r:
                return 0
            # If we've cached this calcuation then return that
            if (l, r) in dp:
                return dp[(l, r)]

            # Iterate from right to left, and compute the result for each case where we pop balloon
            # i last
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                # Add the coins to out total coins if we were popping i last, then the boundaries
                # would be whatever element is beyond out left and right boundaries
                coins = balloons[l - 1] * balloons[i] * balloons[r + 1]
                # If we pop i as last, then we need to add coins we can get from the left subarray
                # and the right subarray
                coins += rec(l, i - 1) + rec(i + 1, r)
                # set dp to be whatever max we could get within these boundaries for each i balloon
                # as last popped
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]

        return rec(1, len(balloons) - 2)
