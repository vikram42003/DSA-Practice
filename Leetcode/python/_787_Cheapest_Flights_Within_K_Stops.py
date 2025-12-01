from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    # Dijkstra + Hop Counting - Time = O(E log V) - Space = O(E + V)
    # We use Dijkstra's + hop counting. Make an adj list like usual and initialize a hops array with inf, which will track the minimum 
    # number of hops it takes to reach that node
    # We need to allow revisiting nodes like in backtracking so we cant really use a seen set, so we'll just count the hops.
    # The heap will naturally make us traverse in the lowest cost path, but during that if the hops > k
    # then we cannot continue down that path and have to skip it. So in order to reconsider the nodes
    # in the prev path, we'll only check if we can reach that node with fewer or equal hops as opposed to membership check in a seen set
    # bestHops only goes down (or stays same) as we progress, and we traverse in lowest-cost order 
    # because of the heap, so we never miss the optimal path. The pruning just avoids redundant work
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        
        # heap stores weight, current hops/k, node
        heap = [(0, 0, src)]
        bestHops = [float("inf")] * n
        bestHops[src] = 0
    
        while heap:
            w, hops, u = heappop(heap)

            if u == dst:
                return w
            
            if hops > k or hops > bestHops[u]:
                continue

            print(f"{u} (w={w}, hops={hops})", end=" -> ")
            bestHops[u] = hops
            for nv, nw in adj[u]:
                heappush(heap, (w + nw, hops + 1, nv))
        
        return -1