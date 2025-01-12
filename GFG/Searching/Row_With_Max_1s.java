// link - https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1

package GFG.Searching;

public class Row_With_Max_1s {
    public int rowWithMax1s(int arr[][]) {
        int max = -1, idx = -1;

        for (int i = 0; i < arr.length; i++) {
            int l = 0, r = arr[i].length - 1;

            while (l <= r) {
                int mid = l + ((r - l) / 2);

                if (arr[i][mid] == 1) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }

            if (max < arr[i].length - l) {
                max = arr[i].length - l;
                idx = i;
            }
        }

        return idx;
    }
}
