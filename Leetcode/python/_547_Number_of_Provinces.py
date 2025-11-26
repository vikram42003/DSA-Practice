from typing import List


class Solution:
    # Union Find - Time = O(n^2) - Space = O(n)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS, COLS = len(isConnected), len(isConnected[0])

        par = list(range(len(isConnected)))

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(u, v):
            pu, pv = find(u), find(v)

            if pu == pv:
                return 0
            else:
                par[pu] = pv
                return 1

        total = len(isConnected)
        for r in range(ROWS):
            for c in range(r + 1, COLS):
                if isConnected[r][c] == 1:
                    total -= union(r, c)

        return total
