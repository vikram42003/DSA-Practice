# Definition of Interval:
import heapq
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    # Greedy and Sort - Time = O(n log n) - Space = O(n)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # First sort the start and end times
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        max_max, cur = 0, 0
        s, e = 0, 0
        # Start will be exhausted before end so that'll be the loop limit
        while s < len(start):
            # If start is less than end then increment cur to signify we are using
            # a new day/room to start a meeting, and look at the next meeting
            # also update max_max
            if start[s] < end[e]:
                s += 1
                cur += 1
                max_max = max(max_max, cur)
            # If start is greater than or equal to end then that means a meeting has
            # ended and that room/day is free, so decrement count
            else:
                e += 1
                cur -= 1

        # Return the max
        return max_max

    # Greedy & Heap - Time = O(n log n) - Space = O(n)
    # The core idea is - we track the meetings in a heap, put the new meeting
    # after the earliest ending meeting and pop out meetings that are done if
    # no conflict, otherwise just only put the new meeting in
    #
    # First sort the intervals by starting time,
    # so that we can start with the earliest meeting, then go through
    # all the meetings and then track whats the earliest end time
    # For our current meeting, if it starts after or at the earliest end
    # time, then we can just do this meeting today and pop it out to
    # signify that the prev meeting (heap[0]) was completed and then add
    # it to the heap
    # Otherwise if it starts before the ealiest one ends then just put it
    # in the heap, this means we'll have to do it on another day and both
    # the overlapping meetings (heap[0] and current) will be present in the heap
    # In the end just return len(res), it'll be the overlapping meetings for each
    # separate day
    #
    # By tracking it this way we ensure that we can (essentially) put the current
    # meeting in any of the days
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        res, heap = 0, []

        for i in intervals:
            if heap and i.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)

        return len(heap)
