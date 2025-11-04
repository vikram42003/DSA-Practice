from collections import deque
from typing import List


# Leetcode 286. Walls and Gates is paywalled, so this is a free version of that exact question but with different phrasing
# Source - https://neetcode.io/problems/islands-and-treasure?list=neetcode150


class Solution:
    # Multi Source BFS - TIme = O(n * m) - Space = O(n * m)
    # Multi Source BFS is just like bfs except we start with multiple root nodes and move deeper for all nodes consecutively.
    # First find all 0's, those will be the roots for the multi source bfs, then run the usual bfs exapnding in all 4 directions
    # For each of 4 directions, add it to bfs if its indices are within bounds and if their value is <= current val + 1, only then overwrite its
    # dist and add it to null to ensure that we only overwrite to make paths shorter not longer
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c = q.popleft()
            dist = grid[r][c] + 1

            for dr, dc in directions:
                if (
                    0 <= r + dr < rows
                    and 0 <= c + dc < cols
                    and grid[r + dr][c + dc] != -1
                    and grid[r + dr][c + dc] > dist
                ):
                    grid[r + dr][c + dc] = dist
                    q.append((r + dr, c + dc))

    # DFS (Likely TLE) - Time = O(m * n * (m + n)) = O(m * n) - Space = (m * n)
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(row, col, dist):
            if (
                row not in range(len(grid))
                or col not in range(len(grid[0]))
                or grid[row][col] == -1
                or grid[row][col] < dist
            ):
                return

            grid[row][col] = dist
            dfs(row + 1, col, dist + 1)
            dfs(row - 1, col, dist + 1)
            dfs(row, col + 1, dist + 1)
            dfs(row, col - 1, dist + 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    dfs(row, col, 0)
