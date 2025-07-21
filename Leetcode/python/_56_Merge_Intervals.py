from typing import List


class Solution:
    # Sorting (Optimized) - Time = O(n log n) - Space = O(n)
    # same as below, except just use prev and cur instead of cur and next
    # update the end values at each step and if cur does not overlap then add prev to res and set prev = cur
    # at the end add prev to res cause it may still hold a value
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        prev = None
        for cur in intervals:
            if not prev:
                prev = cur
                continue

            if prev[1] >= cur[0]:
                prev[1] = max(prev[1], cur[1])
            else:
                res.append(prev)
                prev = cur

        res.append(prev)
        return res

    # Sorting - Time = O(n log n) - Space = O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start = None
        end = -1
        i = 0
        while i < len(intervals) - 1:
            if start == None:
                start = intervals[i][0]

            print(end, intervals[i][1])
            end = max(end, intervals[i][1])

            if intervals[i + 1][0] > end:
                res.append([start, end])
                start = None
                end = -1

            i += 1

        start = intervals[-1][0] if start == None else start
        end = max(end, intervals[-1][1])
        res.append([start, end])

        return res


# sort the list by start values
# take cur[0] as start if start == None
# then check the start for next element
# if next.start <= cur.end, then start remains the same but cur moves forward (this basically means
# we can combine cur and next)
# repeat until len(nums) - 1
# if next.start > cur.end then the previous range is [start, cur.end] and then set start to None
# and move to next element
# EDGECASE - cur.end may be greater than next.end so keep updating that too
