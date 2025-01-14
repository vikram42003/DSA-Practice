// link - https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1

package GFG.Searching;

public class Median_in_a_Row_Wise_Sorted_Matrix {
    int median(int mat[][]) {
        int req = (mat.length * mat[0].length) / 2;
        // search space will definitely be between the smallest element and
        // the largest element
        int l = 1, r = 0;
        for (int i = 0; i < mat.length; i++) {
            l = Math.min(l, mat[i][0]);
            r = Math.max(r, mat[i][mat[i].length - 1]);
        }

        // the median element will have exactly row * col / 2 elements before it
        // but there can be a repetition of the median number
        // so find the first one that has more that row * col / 2 elements
        // before it and then return the element just before it
        // use binary search to count the number of elements
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            int c = count(mat, mid);
            if (c > req) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }

    int count(int[][] mat, int val) {
        int total = 0;
        for (int[] row : mat) {
            int l = 0, r = row.length - 1;
            int idx = row.length;
            while (l <= r) {
                int mid = l + ((r - l) / 2);
                if (row[mid] > val) {
                    idx = mid;
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }

            total += idx;
        }
        return total;
    }
}
