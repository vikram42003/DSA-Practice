from typing import List


class Solution:
    # Backtracking Optimized - Time = O(3 ^ n) - Space = O(n)
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # Edge Case: word length is more than matrix size
        if len(word) > rows * cols:
            return False

        # Optimization: check the board and if the frequency of last letter in word is less
        # than the starting letter, then flip word, that way we'll have to make less dfs searches
        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        seen = set()

        def dfs(r, c, i):
            # Base Case 1: We found the word
            if i == len(word):
                return True

            # Base Case 2: Index out of bounds, invalid match, or word already seen
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or board[r][c] != word[i]
                or (r, c) in seen
            ):
                return False

            # Add to seen
            seen.add((r, c))

            # Recurse
            didWeFindIt = (
                dfs(r - 1, c, i + 1)
                or dfs(r + 1, c, i + 1)
                or dfs(r, c - 1, i + 1)
                or dfs(r, c + 1, i + 1)
            )

            # Remove from seen
            seen.remove((r, c))

            return didWeFindIt

        # Find starting word
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False

    # Backtracking - Time = O(n * 3 ^ L) = O(3 ^ n) - Space = O(n)
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        # Check the adjacent elements until we find the word
        # r - rowIdx   c - colIdx   i = current letter in word we're looking for
        def check(r, c, i):
            # If indices are out of bounds or the current element does not match or we've already visited the current element
            if (
                r < 0
                or r >= len(board)
                or c < 0
                or c >= len(board[0])
                or i < 0
                or i >= len(word)
                or board[r][c] != word[i]
                or (r, c) in seen
            ):
                return False
            # If this is the last letter in word and it matches
            elif i == len(word) - 1:
                return True
            # If word[i] matches but its not the last word then run check for elements above, below
            # left and right of current word with an or condition
            else:
                seen.add((r, c))
                if (
                    check(r - 1, c, i + 1)
                    or check(r + 1, c, i + 1)
                    or check(r, c - 1, i + 1)
                    or check(r, c + 1, i + 1)
                ) == False:
                    seen.remove((r, c))
                    return False
                else:
                    return True

        # Check for starting letter
        for rowIdx in range(len(board)):
            for colIdx in range(len(board[rowIdx])):
                if board[rowIdx][colIdx] == word[0]:
                    if check(rowIdx, colIdx, 0):
                        return True

        return False


test = Solution()

# ans = true
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

# ans = true
board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word2 = "SEE"

# ans = false
board3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word3 = "ABCB"

test.exist(board3, word3)
