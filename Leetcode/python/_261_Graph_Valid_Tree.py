from collections import deque
from typing import List


class Solution:
    # BFS (Optimal) - Time = O(V + E) - Space = O(V + E)
    # A valid tree must have exactly n - 1 edges and all nodes must be connected.
    # Build a bi-directional adjacency list and use a queue of (node, parent) and a seen set starting from 0 for traversal
    # Edge case: return False if len(edges) != n - 1 because in a valid tree, total edges are always 1 less than the total vertices
    # For each neighbor:
    #   - If it's already seen and not the parent, it means its a cycle so return False.
    #   - Else mark it seen and push it to the queue as (child, curr).
    # Finally, return len(seen) == n to check if we visited all nodes.
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = {i: [] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set([0])
        q = deque([(0, -1)])

        while q:
            curr, prev = q.popleft()

            for child in adj[curr]:
                if child == prev:
                    continue

                if child in seen:
                    return False

                seen.add(child)
                q.append((child, curr))

        return len(seen) == n

    # BFS - Time = O(V + E) - Space = O(V + E)
    # Make a bi-directional adjacency matrix (WITH SETS) and add each edge and its inverse ((0, 1) and (1, 0))
    # We'll do BFS so make a deque and a seen set for traversal and add 0 to both, then traverse LEVEL BY LEVEL and
    # loop over curr nodes children and check if any of them are in seen (a cycle is found)
    # Then add child to seen and remove curr from the child's neighbours (adj[child]) (so we dont go back and do an infinite loop)
    # return len(seen) == n to check if we have visited all nodes (unvisited/disconnected node means not a tree)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: set() for i in range(n)}

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        seen = set()
        q = deque()

        q.append(0)
        seen.add(0)

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                for child in adj[curr]:
                    if child in seen:
                        return False

                    adj[child].remove(curr)
                    seen.add(child)
                    q.append(child)

        return len(seen) == n
