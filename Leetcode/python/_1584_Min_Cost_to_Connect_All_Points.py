from heapq import heappop
from typing import List


class Solution:
    # (Unoptimized) Prim's Minimum Spanning Tree - Time = O((V - 1) ^ 2) - Space = O((V - 1) ^ 2)
    # We arent given any edges so we'll work as if it was a complete graph
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        weights = [float("inf")] * len(points)

        def dist(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return abs(x2 - x1) + abs(y2 - y1)

        def hash(p):
            return f"{p[0]}{p[1]}"

        heap = [(dist(points[0], points[0]), points[0])]
        seen = set()
        total = 0

        while heap:
            d, point = heappop(heap)
            if hash(point) in seen:
                continue

            total += d
            seen.add(hash(point))

            for p in points:
                if hash(p) not in seen:
                    heappush(heap, (dist(point, p), p))

        return total
