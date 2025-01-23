from typing import List


class Solution:
    # Merge and stuff - Time = O(n) - Space = O(n) or O(1)
    # We iterate through the intervals while trying to merge the intervals
    # We merge by checking if the end time of prev interval is >= start time of current interval, if true then
    # the start time should be the start time of prev one (since theyre sorted already) and end time should be
    # max of both of their end times. This effectively covers the cases of current interval bein completely
    # covered by or extending prev
    # The only special thing is where to insert newInterval, but since we have to mantain the ascending order of
    # start times, we insert newInterval where the first time newInterval start time exceeds current interval
    # start time and we follow the same merge logic when inserting newInterval, and we track if we've inserted
    # newInterval or not
    # Any subsequent offsets to the intervals are processed as normal.
    # In the end if we see that we havent inserted newInterval then we insert it at the end according to the same
    # merge logic we used earlier
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res, didWeUseNewInterval = [], False

        for i in intervals:
            if not didWeUseNewInterval and i[0] > newInterval[0]:
                if res and res[-1][1] >= newInterval[0]:
                    res[-1][1] = max(res[-1][1], newInterval[1])
                else:
                    res.append(newInterval[:])
                didWeUseNewInterval = True

            if res and res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)

        if not didWeUseNewInterval:
            if res and res[-1][1] >= newInterval[0]:
                res[-1][1] = max(res[-1][1], newInterval[1])
            else:
                res.append(newInterval[:])

        return res


# [[1,2],[3,5],[6,7],[8,10],[12,16]]   [4,8]
# [[1,2],[3,5],[4,8],[6,7],[8,10],[12,16]]
# [[1,2],[3,8],[6,7],[8,10],[12,16]]
# [[1,2],[3,8],[8,10],[12,16]]
# [[1,2],[3,10],[12,16]]
