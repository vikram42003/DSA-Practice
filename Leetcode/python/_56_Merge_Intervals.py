from typing import List


class Solution:
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
