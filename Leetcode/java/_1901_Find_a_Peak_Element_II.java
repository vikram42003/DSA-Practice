// link - https://leetcode.com/problems/find-a-peak-element-ii/

public class _1901_Find_a_Peak_Element_II {
    public static void main(String[] args) {
        int[][] mat = {
                { 70, 50, 40, 30, 20 },
                { 100, 1, 2, 3, 4 }
        };

        System.out.println(findPeakGridBS(mat));
    }

    // Binary Search - O(n log(m))
    public static int[] findPeakGridBS(int[][] mat) {
        int l = 0, r = mat[0].length - 1;
        while (l <= r) {
            int mid = l + ((r - l) / 2);

            int max = 0;
            for (int i = 0; i < mat.length; i++) {
                if (mat[max][mid] < mat[i][mid])
                    max = i;
            }

            int left = mid - 1 >= 0 ? mat[max][mid - 1] : -1;
            int right = mid + 1 < mat[0].length ? mat[max][mid + 1] : -1;

            if (mat[max][mid] > left && mat[max][mid] > right) {
                return new int[] { max, mid };
            } else if (left < right) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return new int[] { -1, -1 };
    }

    // Iterative Solution
    public int[] findPeakGrid(int[][] mat) {
        int row = 0, col = 0;

        while (true) {
            int curr = mat[row][col];
            int up = row - 1 >= 0 ? mat[row - 1][col] : -1;
            int down = row + 1 < mat.length ? mat[row + 1][col] : -1;
            int left = col - 1 >= 0 ? mat[row][col - 1] : -1;
            int right = col + 1 < mat[row].length ? mat[row][col + 1] : -1;

            if (curr < up) {
                row--;
            } else if (curr < down) {
                row++;
            } else if (curr < left) {
                col--;
            } else if (curr < right) {
                col++;
            } else {
                return new int[] { row, col };
            }
        }
    }
}
