from collections import deque
from typing import List


class Solution:
    # Kahn's Algo Topological Sort - Time = O(3V + V + E) = O(V + E) = O(n) - Space = O(2V + E) = O(V + E) = O(n) (verify the extended space and time again)
    # We see whether Topological sorting with Kahn's algorithm would have printed nodes == numCourses or not. Topological sorting in graphs is just 
    # dfs + print/action at the deppest level, bubbling up.
    # Kahs's Algorithm variant is - first make an adjacency graph for all vertices and edge direction, and indegree (how many edges points to current)
    # then do a multi source BFS with all indegree[i] == 0, remove all the edges that originate from this current vertex from indegree for all current's edges
    # and add indegree[i] to the queue if its its value is 0, repeat until all inorder[i] == 0 (success) or all inorder[i] > 0 (fail, because of cycle) 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjacency graph - list of all courses where B -> A, and B is the prerequisite we need to finish, before we go to A
        adj = {i: [] for i in range(numCourses)}
        # indegree of a vertex, where indegree[i] is the number of edges pointing to vertex i
        indegree = [0] * numCourses

        # plot the adj chart and inorder
        for course, preq in prerequisites:
            adj[preq].append(course)
            indegree[course] += 1

        # put the base vertices into the queue (where no edges are pointing to it)
        q = deque([i for i in range(len(indegree)) if indegree[i] == 0])

        canComplete = 0
        while q:
            curr = q.popleft()
            canComplete += 1
            for v in adj[curr]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return canComplete == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map course to prerequisite
        courseMap = {i: [] for i in range(numCourses)}
        for c, pre in prerequisites:
            courseMap[c].append(pre)

        # A set to track circular dependencies and completed courses so we dont double count
        seen, completed = set(), set()

        def dfs(prerequisite):
            # Its a circular dependency
            if prerequisite in seen:
                return False
            # We already know this one can be completed so early exit
            if prerequisite in completed:
                return True

            seen.add(prerequisite)
            for pre in courseMap.get(prerequisite, []):
                if not dfs(pre):
                    return False
            seen.remove(prerequisite)
            completed.add(prerequisite)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
