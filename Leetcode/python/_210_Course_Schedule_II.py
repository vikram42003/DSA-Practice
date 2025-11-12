from collections import deque
from typing import List


class Solution:
    # Kahn's Algo Topo Sort - Time = O(V + E) - Space = O(V + E)
    # check this article for more details - https://mohammad-imran.medium.com/understanding-topological-sorting-with-kahns-algo-8af5a588dd0e
    # We see whether Topological sorting with Kahn's algorithm would have printed nodes == numCourses or not. Topological sorting in graphs is just
    # dfs + print/action at the deepest level, bubbling up.
    # Kahs's Algorithm variant is - first make an adjacency graph for all vertices and edge direction, and indegree (how many edges points to current)
    # then do a multi source BFS with all indegree[i] == 0, remove all the edges that originate from this current vertex from indegree for all current's edges
    # and add indegree[i] to the queue if its its value is 0, repeat until all inorder[i] == 0 (success) or all inorder[i] > 0 (fail, because of cycle)
    # An additional thing we do is append the curr node to res, and return res if canComplete == numCourses else []
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, preq in prerequisites:
            adj[preq].append(course)
            indegree[course] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        canComplete = 0
        while q:
            curr = q.popleft()
            canComplete += 1
            res.append(curr)
            for v in adj[curr]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return res if canComplete == numCourses else []
