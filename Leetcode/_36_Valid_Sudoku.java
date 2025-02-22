// link - https://leetcode.com/problems/valid-sudoku/

public class _36_Valid_Sudoku {
    // Time = O(1) - Space = O(1)
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] grid = new boolean[9][9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.')
                    continue;

                int num = board[i][j] - 1;
                if (rows[i][num] == true || cols[j][num] == true || grid[i + num % 3][j + num % 3] == true) {
                    return false;
                }
                rows[i][num] = true;
                cols[j][num] = true;
                grid[i + num % 3][j + num % 3] = true;
            }
        }

        return true;
    }
}
