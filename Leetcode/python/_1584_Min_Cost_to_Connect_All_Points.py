from heapq import heappop, heappush
from typing import List


class Solution:
    # Prim's (Optimized) - Time = O(V ^ 2) - Space = O(V)
    # Since this is a connected graph and every vertex has an edge to every other vertex, we'll mantain weights and seen lists, both of size n
    # Weights will be initialized with inf for all edges and seen will be False
    # Start by adding any initial edge to weights with weight 0 and set seen for that node to True
    # We'll iterate n times, one for each vertex, and in each loop we will select the minimum unseen weight, set it as seen and add its weight to total
    # and then we'll update the dist for each node from this current node, for each unseen node, updating dist if its smaller
    # and in the end return total
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        weights = [float("inf")] * n
        weights[0] = 0

        seen = [False] * n
        total = 0

        for _ in range(n):
            smallest = float("inf")
            idx = -1

            for i in range(n):
                if seen[i] == False and weights[i] < smallest:
                    smallest = weights[i]
                    idx = i

            total += smallest
            seen[idx] = True

            for i in range(n):
                if not seen[i]:
                    d = dist(points[idx], points[i])
                    if d < weights[i]:
                        weights[i] = d

        return total

    # (Unoptimized) Prim's Minimum Spanning Tree - Time = O(V^2 Log V) - Space = O(V ^ 2)
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
