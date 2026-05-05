from typing import List


class Solution:
    # Monotonic Stack - Time = O(n) - Space = O(n)
    # We have to wait for warmer temperature, so we can basically see a monotonic pattern in the input data - the temperature should be increasing
    # So that's what we do, we initialize a descending monotonic stack. Why descending? because if the
    # temperature drops, then we keep appending that to the stack and waiting until an increase in
    # temperature comes and breaks that pattern, after putting that new increased temperature we do the
    # same again, keep waiting if the temp is decreasing and start popping and recording the days passed if its increasing

    # So we init a res array, have a monotonic stack that will only track the indices (for convenience),
    # have the monotonic decrease mantaining condition, pop element if we see an increase, track the diff
    # bw the popped element and cur element in res and return ress
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        # monotonically descending stack
        stack = []
        for i in range(len(temperatures)):
            # When we see a larger element we pop cur head
            # and track the number of indices the popped element is away from i
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res
