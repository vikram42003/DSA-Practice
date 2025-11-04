from typing import List


class Solution:
    # DFS (Edges to center) - Time = (n * m) - Space = O(n * m)
    # The core idea is that, instead of going from each cell and checking all sides recursively with dfs to see if it can reach both the oceans,
    # We start our search from the boundaries (top row, bot row, left col, right col), where its guarenteed its touching the ocean, from that we run the dfs
    # And we track each cell with its corresponding ocean set, so theres no redundant traversal, and we only proceed with the dfs if its a valid cell
    # ie. index within bounds, prev height < curr height, curr not in set
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, prev, ocean):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or prev > heights[r][c]
                or (r, c) in ocean
            ):
                return

            ocean.add((r, c))
            dfs(r + 1, c, heights[r][c], ocean)
            dfs(r - 1, c, heights[r][c], ocean)
            dfs(r, c + 1, heights[r][c], ocean)
            dfs(r, c - 1, heights[r][c], ocean)

        # Add the first row to pacific set and last row to atlantic set through dfs
        # DFS will automatically make it expand to as far it can go
        for c in range(COLS):
            dfs(0, c, -1, pacific)
            dfs(ROWS - 1, c, -1, atlantic)

        # Add the first col to pacific set and last col to atlantic set through dfs
        # DFS will automatically make it expand to as far it can go
        for r in range(ROWS):
            dfs(r, 0, -1, pacific)
            dfs(r, COLS - 1, -1, atlantic)

        # Intersection of sets
        return [[r, c] for r, c in pacific & atlantic]

    # DFS (Really slow) - Time = O((m * n) ^ 2) - Space = O(m * n)
    # Run a dfs from each cell and keep track of an oceans set, clear it on start and then during dfs if we hit an oeacns bounds add that oean to the
    # oceans set. After running dfs add the cell to result if oceans set contains both oceans.
    # Also keep track of seen so we dont bounce around cells of same value infinitely
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        rows, cols = len(heights), len(heights[0])

        # oceans - a set of the oceans current cell can flow into
        oceans, seen = set(), set()

        def dfs(row, col, prev):
            if (row, col) in seen:
                return

            if row < 0 or col < 0:
                oceans.add("pacific")
                return
            elif row >= rows or col >= cols:
                oceans.add("atlantic")
                return

            if heights[row][col] > prev or len(oceans) == 2:
                return

            seen.add((row, col))

            dfs(row + 1, col, heights[row][col])
            dfs(row - 1, col, heights[row][col])
            dfs(row, col + 1, heights[row][col])
            dfs(row, col - 1, heights[row][col])

            seen.remove((row, col))

        for r in range(rows):
            for c in range(cols):
                oceans.clear()
                seen.clear()

                dfs(r, c, heights[r][c])

                if len(oceans) == 2:
                    result.append([r, c])

        return result
