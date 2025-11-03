from collections import deque
from typing import List


class Solution:
    # DFS - Time = O(n * m * 4^d) - Space = O(n)
    # Time - n * m = dimensions of the matrix
    #      - 4 ^ D = all 4 direcyions we can move
    # Space - n = recursion stack space

    # Whenever we encounter an island ("1"), run a dfs with all 4 directions to mark the entire island "#" for visited and increment res. Then go find the next island
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(row, col):
            if (
                row < 0
                or row == len(grid)
                or col < 0
                or col == len(grid[0])
                or grid[row][col] != "1"
            ):
                return

            grid[row][col] = "#"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    res += 1

        return res

    # BFS version - (bit slower than dfs)
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            grid[row][col] = "#"

            while q:
                r, c = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc
                    if (0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == "1"):
                        grid[newRow][newCol] = "#"
                        q.append((newRow, newCol))
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    bfs(row, col)
                    res += 1
        
        return res
