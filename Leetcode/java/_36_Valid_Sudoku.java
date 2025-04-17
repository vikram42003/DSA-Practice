// link - https://leetcode.com/problems/valid-sudoku/

// For checking for the 3X3 grid, pick each element and place it at its correct position in 
// that elements grid
// We do that by first finding out where the current grid starts and then checking the current number
// and then moving 'current number spaces' in the grid (eg. if the element was 5, then we'd find 
// the start of the grid and move 5 spaces left to right, top to bottom)

// gird starts
// 00   03   06
// 30   33   36
// 60   63   66

// for 8 which is at [3][0] and should be at [5][1]
// Sub-grid start 
//     i = (i / 3) * 3 = (3 / 3) * 3 = 1 * 3 = 3
//     j = (j / 3) * 3 = (0 / 3) * 3 = 0 * 3 = 0
//     sub grid start = [3][0]
// position for 8 in this subgrid
//     (here i and j are sub grid i and j)
//     (val = val - 1 becuase of 0 indexing)
//     i += 7 / 3 = 2          i = 3 + 2 = 5
//     j += 7 % 3 = 1          j = 0 + 1 = 1
//     position should be [5][1]

// for 6 which is at [3][4] and should be at [4][5]
// sub grid pos
//     i = (3 / 3) * 3 = 1 * 3 = 3
//     j = (4 / 3) * 3 = 1 * 3 = 3
//     sub grid start = [3][3]
// position for 6 in this subgrid
//     i += 5 / 3 = 1          i = 3 + 1 = 4
//     j += 5 % 3 = 2          j = 3 + 2 = 5
//     position should be [4][5]

public class _36_Valid_Sudoku {
    // Time = O(9^2) = O(1) - Space = O(3 * 9^2) = O(1)
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] grid = new boolean[9][9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.')
                    continue;

                int num = board[i][j] - '0' - 1;

                // Find the grid start
                int grid_i = (i / 3) * 3;
                int grid_j = (j / 3) * 3;
                // Move 'num' spaces forward within the current grid
                // divide will give us vertical position and modulus will give us horizontal
                // position
                grid_i += num / 3;
                grid_j += num % 3;

                if (rows[i][num] == true || cols[j][num] == true || grid[grid_i][grid_j] == true) {
                    return false;
                }
                rows[i][num] = true;
                cols[j][num] = true;
                grid[grid_i][grid_j] = true;
            }
        }

        return true;
    }
}
