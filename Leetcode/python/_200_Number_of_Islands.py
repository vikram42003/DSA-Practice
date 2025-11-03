from typing import List


class Solution:
    # DFS - Time = O(n * m * 4^d) - Space = O(n)
    # Time - n * m = dimensions of the matrix
    #      - 4 ^ D = all 4 direcyions we can move
    # Space - n = recursion stack space

    # Whenever we encounter an island ("1"), run a dfs to mark the entire island "#" for visited and increment res. Then go find the next island
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
