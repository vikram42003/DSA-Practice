from heapq import heappop, heappush
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        for i, ma in enumerate(mat):
            sol = self.binarySearch(ma)
            heappush(heap, (sol, i))

        res = [heappop(heap)[1] for _ in range(k)]
        return res

    def binarySearch(self, mat: List[int]) -> int:
        l, r = 0, len(mat) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mat[mid] == 1:
                l = mid + 1
            else:
                r = mid - 1

        return l
