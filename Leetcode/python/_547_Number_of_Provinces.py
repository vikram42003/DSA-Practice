from typing import List


class Solution:
    # DFS - Time = O(n^2) - Space = O(n)
    # Make a seen array for each city and iterate from city 0 to n and see if its not seen then run a dfs with that if its not seen, update seen to denote we've seen this, and increment the total
    # In the matrix, each row will denote the cities the current row (current city) can reach so in
    # the dfs we'll iterate over [city][i] and if its 1, denoting a connection and its not in seen,
    # then we'll put it in seen and run a dfs on the city it connects to
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = [0] * n

        def dfs(city):
            for reachableCity in range(n):
                if isConnected[city][reachableCity] == 1 and seen[reachableCity] == 0:
                    seen[reachableCity] = 1
                    dfs(reachableCity)

        # Each row i in isConnected will tell us which city the current city can reach (if isConnected[city][i] == 1, then city can reach the ith city)
        total = 0
        for city in range(n):
            if not seen[city]:
                seen[city] = 1
                dfs(city)
                total += 1

        return total

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
