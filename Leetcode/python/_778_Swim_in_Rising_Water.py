from heapq import heappop, heappush
from typing import List


class Solution:
    # Dijkstra - Time = O(n^2 log n) - Space = O(n^2)
    # Start Dijkstra from top left, traverse in all directions, selecting shortest path and end when we hit bottm right.
    # For distance, we'll just track the time/weight we need to traverse that particular neighbour by doing max(w, grid[nr][nc]) because
    # we dont need to do culminative distance since the problem statement states that we can travel infinite distance as long as grid[i][j] <= t
    # So thats why we only need to return the max value of grid[i][j] we see in the shortest path from top left to bottom right
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            w, r, c = heappop(heap)
            if (r, c) in seen:
                continue

            if r == n - 1 and c == n - 1:
                return w

            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in seen and 0 <= nr < n and 0 <= nc < n:
                    heappush(heap, (max(w, grid[nr][nc]), nr, nc))

        return -1

    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        heap = [(grid[0][0], (0, 0))]
        seen = set()

        def hash(i, j):
            return f"{i}{j}"

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        t = 0
        while t <= 2500:
            w, coords = heappop(heap)
            if t < w:
                t = w
            i, j = coords
            # print(grid[i][j], end=" -> ")
            if i == ROWS - 1 and j == COLS - 1:
                return t

            if hash(i, j) in seen:
                continue

            seen.add(hash(i, j))

            for x, y in directions:
                a = i + x if 0 <= i + x < ROWS else -1
                b = j + y if 0 <= j + y < COLS else -1
                if hash(a, b) not in seen and a != -1 and b != -1:
                    heappush(heap, (grid[a][b], (a, b)))

        return -1
