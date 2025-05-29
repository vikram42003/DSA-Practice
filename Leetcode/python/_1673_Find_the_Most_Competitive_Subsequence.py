from typing import List


class Solution:
    # Monotonic Stack - Time = O(n) - Space = O(n)

    # Just keep an ascending monotonic stack
    # We need to find the comnbination which has the digits minimum in value from left to right, so basically an ascending combination
    # so keep the stack monotonic, if n keeps the stack ascending, add it!, if it doesnt, pop it (and keep popping it while the while
    # loop conditions are true)
    # But also the subarray needs to be of size k, which means we can only pop len(nums) - k digits
    # and if were left with any leftover digits, meaning k > 0, it means that the current stack is ascending but has more digits than
    # it needs, and to make it of size k while keeping its value minimim we can remove k digits from the right, since the larger
    # digits will be to the right
    # and we'll have our answer!

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # ascending monotonic stack
        stack = []

        k = len(nums) - k
        for n in nums:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        while k:
            stack.pop()
            k -= 1

        return stack
