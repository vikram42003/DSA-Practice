from typing import List


class Solution:
    # DFS - Time = O(r * c) - Space = O(r * c)
    # Time - r * c = dimensions of the matrix, we mark the visited as "#", so this is basically what it is about
    # Space - r * c = dimensions of the matrix again, cause if the entire matrix was filled then we'd have to recurse r * c times

    # Whenever we encounter an island ("1"), run a dfs with all 4 directions to mark the entire island "#" for visited and track cur_max and max_max. Then go find the next island
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_max, cur_max = 0, 0

        def dfs(row, col):
            if not (
                0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0
            ):
                return

            nonlocal cur_max, max_max
            cur_max += 1
            max_max = max(max_max, cur_max)
            grid[row][col] = 0

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    cur_max = 0
                    dfs(row, col)

        return max_max
