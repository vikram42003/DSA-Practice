from typing import List


class Solution:
    # DFS - Time = O(E + V) - Space = O(E + V)
    # Start a DFS/BFS at every unvisited node; each start is one connected
    # component, and the DFS just marks all nodes in that component as seen
    # cycles don’t matter.
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set()

        def dfs(i):
            seen.add(i)
            for j in adj[i]:
                if j not in seen:
                    dfs(j)

        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)

        return count
