import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            largest = -1 * heapq.heappop(heap)
            second_largest = -1 * heapq.heappop(heap)

            if largest != second_largest:
                largest -= second_largest
                heapq.heappush(heap, -largest)

        if len(heap) > 0:
            return -heap[0]
        else:
            return 0