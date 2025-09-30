from typing import List


class Solution:
    # Backtracking - Time = O(n * 3 ^ L) = O(3 ^ n) - Space = O(n)
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        # Check the adjacent elements until we find the word
        # r - rowIdx   c - colIdx   i = current letter in word we're looking for
        def check(r, c, i):
            # If indices are out of bounds or the current element does not match or we've already visited the current element
            if (
                r < 0 or r >= len(board)
                or c < 0 or c >= len(board[0])
                or i < 0 or i >= len(word)
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
