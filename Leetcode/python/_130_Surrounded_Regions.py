from typing import List


class Solution:
    # DFS (Boundary) - Time = O(n * m + n * m) = O(n * m) - Space = O(n * m)
    # Time - n * m for dfs worse case (we mark visited as "#" so we only do n * m with dfs on worst case)
    #      - n * m another time for the final board traversal
    # Space - n * m for stack space incase we have to do dfs that covers the entire board in worst case

    # Any region of O cannot be flipped if its connected to the boundares, so we just check from the boundaries
    # Find the starting of a region on the row and col boundaries, and then mark the entire region as "#"
    # so we definitely know we cant flip it, then the regions of "O"'s which are left would be "islands", which we can flip
    # Then just go through the array and flip those, and also turn the invalid regions we changed to "#" back to "O"
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
