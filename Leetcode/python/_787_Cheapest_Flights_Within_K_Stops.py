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
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
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

    # Bellman Ford - Time = O(E * (K + 1)) - Space = O(n)
    # We'll use the Bellman Ford algorithm, with a little bit of customization (since there are no
    # negative edges, but we do have egde hop limit)
    # First initialize a list of prices for each node with inf for all edges except src which is 0
    # Then for each hop, from i to k + 1 (k + 1 because if k = 0 we need to run the loop 1 time),
    # update the price in a temp array for all the edges we can reach from current hop limit
    # Skip any edge which is outside the current i hop limit by checking for prices[f] == inf
    # Eg. for A -> B, A -> C, B -> C, then for i == 0, we can process A -> B and A -> C but not B -> C
    # because that is 1 more hop so its prices[f] value will be inf to denote that, same for
    # succeeding edges, but in the next i value, it will be accessible, change through prices
    # being updated with temp
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices[:]
            for f, t, p in flights:
                if prices[f] == float("inf"):
                    continue
                elif prices[f] + p < temp[t]:
                    temp[t] = prices[f] + p
            prices = temp

        return -1 if prices[dst] == float("inf") else prices[dst]
