// link - https://leetcode.com/problems/search-a-2d-matrix/description/

public class _74_Search_a_2D_Matrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rowL = 0, rowR = matrix.length - 1;
        int row = 0;
        while (rowL <= rowR) {
            int mid = rowL + ((rowR - rowL) / 2);
            if (matrix[mid][0] == target) {
                row = mid;
                break;
            } else if (matrix[mid][0] < target) {
                row = mid;
                rowL = mid + 1;
            } else {
                rowR = mid - 1;
            }
        }

        int colL = 0, colR = matrix[row].length - 1;
        int col = 0;
        while (colL <= colR) {
            int mid = colL + ((colR - colL) / 2);
            if (matrix[row][mid] == target) {
                col = mid;
                break;
            } else if (matrix[row][mid] < target) {
                colL = mid + 1;
            } else {
                colR = mid - 1;
            }
        }

        return matrix[row][col] == target;
    }
}
