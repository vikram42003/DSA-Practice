from heapq import heappop, heappush
from typing import List


class Solution:
    # Dijkstra - Time = O(n^2 log n) - Space = O(n^2)
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
