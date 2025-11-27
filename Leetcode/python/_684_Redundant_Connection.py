from typing import List


class Solution:
    # Union Find - Time = O(α(n)) = O(n) - Space = O(n)
    # The graph was initially a tree so each node WILL NOT have the same parent when we're building the tree otherwise there would be a cycle
    # If two nodes have the same parent then connecting them would cause a cycle, and it would
    # disqualify the tree property of the graph, so return the last one that causes a cycle
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = list(range(len(edges) + 1))

        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]

        res = None

        def union(u, v):
            nonlocal res
            pu, pv = find(u), find(v)
            if pu == pv:
                res = [u, v]
            par[pv] = pu

        for u, v in edges:
            union(u, v)

        return res
