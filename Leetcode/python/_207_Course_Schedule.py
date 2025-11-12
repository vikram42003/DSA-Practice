from typing import List


class Solution:
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
