from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    # Dijkstra - Time = O(V log E) - Space = O(E + V)
    # make an adj list then use Dijkstra's algo. Create a min heap and seen, heap will store the shortest path to n and have entries like (cost, node)
    # Initialize heap with (0, k), then iterate while heap and pop the smallest item out of the heap, we first check if we've already seen it, 
    # then that means that we have locked in its dist (since we always pop the shortest path to node N out of the heap, so if we're seeing it 
    # again then that means shortest path has been locked in)
    # For each node we pop, keep track of its cost with a res variable and keep updating it
    # then add it to seen and iterate over its neighbours, and add those to the heap with (curDist + neighbourDist, neighbour) only if the neighbour
    # is not in seen
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        heap = [(0, k)]
        seen = set()
        res = 0

        while heap:
            curW, curN = heappop(heap)
            if curN in seen:
                continue

            seen.add(curN)
            res = max(res, curW)

            for neighbourN, neighbourW in adj[curN]:
                if neighbourN not in seen:
                    heappush(heap, (curW + neighbourW, neighbourN))

        return res if len(seen) == n else -1
