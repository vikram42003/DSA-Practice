from typing import List


class Solution:
    # Greedy - Time = O(n) - Space = O(1)
    # Just track the max distance we can reach, if our current i index crosses what we calculated to be the max reachable
    # distance then return false, otherwise true
    def canJump(self, nums: List[int]) -> bool:
        maxReach, n = 0, len(nums)
        for i in range(n):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        return True

    def canJump(self, nums: List[int]) -> bool:
        nextSpot, n, i = 0, len(nums), 0
        while i <= nextSpot and i < n:
            nextSpot = max(nextSpot, i + nums[i])
            i += 1
        return i >= n
