// link - https://leetcode.com/problems/search-a-2d-matrix/description/

// 1 3 5 7 10 11 16 20 23 30 34 60

public class _74_Search_a_2D_Matrix {
    public static void main(String[] args) {
        int[][] matrix = { { 1, 3, 5, 7 }, { 10, 11, 16, 20 }, { 23, 30, 34, 60 }}; // ans = false
        int target = 13;

        System.out.println(searchMatrix(matrix, target));
    }
    
    public static boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) return false;

        int l = 0, r = matrix.length * matrix[0].length - 1;
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            int curr = matrix[mid / matrix[0].length][mid % matrix[0].length];
            if (curr == target) {
                return true;
            } else if (curr < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        
        return false;
    }

    public boolean searchMatrixBinarySearch(int[][] matrix, int target) {
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
