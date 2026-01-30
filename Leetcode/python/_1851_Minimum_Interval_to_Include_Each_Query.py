from typing import List


class Solution:
    # Sweep Line + Min Heap - Time = O((n + q) log n) - Space = O(n)
    # The core idea is to reuse work across queries instead of recomputing from scratch.
    # Queries are sorted so that we can move monotonically from left to right. Intervals are also sorted
    #
    # Since queries can be processed in any order, we sort them and sweep from left to right.
    # As q increases, intervals only ever become valid once (start <= q) and then become
    # permanently invalid once (end < q), so we can maintain a rolling candidate set.
    #
    # We'll sort intervals by start and add all intervals whose start <= current q into a min heap.
    # The heap stores (interval_length, interval_end) so that:
    #   - interval_length lets us always pick the smallest valid interval
    #   - interval_end lets us lazily remove intervals that can no longer cover q
    #
    # For each query:
    #   - Add all newly eligible intervals (start <= q)
    #   - Remove all intervals that have expired (end < q), since they cannot be answers
    #     for this q or any future queries
    #   - The heap top now represents the minimum-length interval that covers q
    #
    # Note: We do NOT pop the heap after answering, since the same interval might still be
    # valid and optimal for subsequent queries.
    # 
    # Check out this chat (especiall the 1️⃣ What “sweep line” actually means (de-mystified) part)
    # https://chatgpt.com/c/697cb788-8220-8323-aa7c-a61e8da42ae3
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[1])
        queries.sort()
        res = {}
        for q in queries:
            res[q] = float("inf")

        # for j in queries:

        m, n = len(intervals), len(queries)
        i, j = 0, 0
        while i < m and j < n:
            while i < m and queries[j] > intervals[i][1]:
                i += 1

            while (
                i < m
                and queries[j] > intervals[i][0]
                and not intervals[i][1] > queries[j]
            ):
                res[queries[j]] = min(
                    res[queries[j]], intervals[i][1] - intervals[i][0] + 1
                )
                i += 1

            if i >= m:
                break

            if intervals[i][0] == queries[j] <= intervals[i][1]:
                res[queries[j]] = min(
                    res[queries[j]], intervals[i][1] - intervals[i][0] + 1
                )
            j += 1

        return [res[q] if res[q] != float("inf") else -1 for q in queries]

test = Solution()
# ans = [3,3,1,4]
# intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
# queries = [2, 3, 4, 5]
# print(test.minInterval(intervals, queries))

# ans = [2,-1,4,6]
intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
queries = [2, 19, 5, 22]
print(test.minInterval(intervals, queries))
