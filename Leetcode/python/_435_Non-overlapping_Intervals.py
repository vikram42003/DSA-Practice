from typing import List


class Solution:
    # Greedy - Time = O(n log n) - Space = O(n)
    # The main idea is, we sort the intervals, and then when we see an overlap, we keep the one that
    # ends earlier to minimize the changes of it overlapping with the next element
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # First sort the intervals
        intervals.sort()
        # Then we track the end value, this end value will represent the final end value for the
        # element right before the current element we're comparing AFTER doing/simulating the removal
        # up until the prev element
        # In the beginning it'll just be the end value of the first interval in our sorted list
        prevEnd = intervals[0][1]

        res = 0

        # Iterate through the intervals starting from idx 1
        for start, end in intervals[1:]:
            # If the current element start and prevEnd dont overlap, then just update prevEnd and continue
            if start >= prevEnd:
                prevEnd = end
            # Otherwise if there is an overlap, then just keep whichever of the two compared intervals
            # that ends earlier, this way we minimize the chances of it overlapping with the elements
            # after it
            # Also increment res to represent us removing one of the values
            else:
                res += 1
                prevEnd = min(prevEnd, end)

        return res
