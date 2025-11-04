from collections import deque
from typing import List


class Solution:
    # Multi Source BFS - Time = O(m * n) - Space = O(m * n)
    # Just run a multi source bfs, and track the number of fresh fruits. while q and fruits > 0, then go down level by level in bfs with for _ in range(len(q))
    # and increment time everytime we go down a level. In the end return -1 if there are fresh fruits left, otherwise return time
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    if (
                        0 <= r + dr < rows
                        and 0 <= c + dc < cols
                        and grid[r + dr][c + dc] == 1
                    ):
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
                        q.append((r + dr, c + dc))
            time += 1

        return time if fresh == 0 else -1
