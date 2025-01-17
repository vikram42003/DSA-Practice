// link - https://www.geeksforgeeks.org/problems/merge-sort/1

package GFG.Basics;

import java.util.Arrays;

public class Merge_Sort {
    public static void main(String[] args) {
        int[] arr = { 4, 1, 3, 9, 7 };
        mergeSort(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }

    public static void mergeSort(int arr[], int l, int r) {
        if (l == r)
            return;
        int mid = l + ((r - l) / 2);
        mergeSort(arr, l, mid);
        mergeSort(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }

    public static void merge(int[] arr, int l, int mid, int r) {
        int[] res = new int[r - l + 1];
        int idx = 0;

        int i = l, j = mid + 1;
        while (i <= mid && j <= r) {
            if (arr[i] < arr[j]) {
                res[idx] = arr[i];
                idx++;
                i++;
            } else {
                res[idx] = arr[j];
                idx++;
                j++;
            }
        }

        while (i <= mid) {
            res[idx] = arr[i];
            idx++;
            i++;
        }
        while (j <= r) {
            res[idx] = arr[j];
            idx++;
            j++;
        }

        for (int k = 0; k < res.length; k++) {
            arr[l + k] = res[k];
        }
    }
}
