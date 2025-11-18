from typing import List


class Solution:
    # Union Find - Time = O(n + m) - Space = O(n)
    # Where time for 
    #   - find = O(α(n))
    #   - union - O(α(n)) 
    #   - n for array initialization and m for traversal over all edges
    # (α denotes a Reverse Ackermann function, which is very close to constant time)
    # 
    # Idea behind Union-Find:
    # - Initially, each node is its own parent (each node is its own component).
    # - We also keep a "rank" array that stores the size of each component's root.
    #
    # - For every edge [a, b], we check if their roots are the same:
    #       If yes → they're already in one component.
    #       If no  → this edge connects two different components, so we merge them.
    #
    # - We merge smaller component into the bigger one (union by size) by attaching
    #   the smaller root to the bigger root and adding their sizes.
    #
    # - During find(), we apply path compression:
    #       We recursively climb up until we find the root,
    #       and along the way we set each node's parent directly to the root.
    #   This flattens the structure, making all future finds extremely fast.
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        rank = [1] * n

        def find(node):
            if node != par[node]:
                par[node] = find(par[node])
            return par[node]

        def union(u, v):
            par_u, par_v = find(u), find(v)

            if par_u == par_v:
                return 0
            elif rank[par_u] > rank[par_v]:
                par[par_v] = par_u
                rank[par_u] += rank[par_v]
            else:
                par[par_u] = par_v
                rank[par_v] += rank[par_u]
            return 1

        count = n
        for u, v in edges:
            count -= union(u, v)

        return count

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
