from typing import List


class Solution:
    # Greedy - Time = O(n) - Space = O(1)
    # Count the jumps, and just stick with the current reach, and also keep a track of the max we can
    # reach, first go as far as its possible within our current reach, but if we are at the last
    # reachable element, only then update the current reach with the maxReach we we're calculating
    # and increment jumps
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps, curReach, maxReach = 0, 0, 0

        for i in range(n - 1):
            maxReach = max(maxReach, i + nums[i])
            if i == curReach:
                curReach = maxReach
                jumps += 1

        return jumps

    # Greedy Solution - Time = O(n) - Space = O(1)

    # I only realized it after writing it but this is like bfs, but the current node is the one we start with
    # and the child nodes are all the nodes we can jump to
    # for nums = [2, 3, 1, 1, 4]
    #                                                   2
    #                                           3              1
    #                                       1   1   4          1
    #
    # We start with 2
    # If we can jump from 2 to the end of the array (i + nums[i] >= len(nums) - 1) then just add this jump to jumps and return it
    # Otherwise, the numbers we can jump to from 2 are 3 and 1
    # We check both child nodes and see that 3 is greater so well jump to that and take it as root and repeat the above steps
    # For 3 we can jump to 1 and 1 and 4
    # BUT we see that this jump can directly let us go to the end of the array, so we'll just do jumps += 1 and return it
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        prev_max = nums[0]
        cur_max = 0

        i = 1
        while i < len(nums):
            if prev_max >= len(nums) - 1:
                jumps += 1
                break

            while i <= prev_max:
                cur_max = max(cur_max, i + nums[i])
                i += 1

            jumps += 1
            prev_max = cur_max

        return jumps
