// link - https://www.geeksforgeeks.org/problems/quick-sort/1

package GFG.Basics;

import java.util.Arrays;

public class Quick_Sort {
    public static void main(String[] args) {
        int[] arr = { 4, 1, 3, 9, 7 };
        quickSort(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }

    static void quickSort(int arr[], int low, int high) {
        if (low < high) {
            int p = partition(arr, low, high);
            quickSort(arr, low, p - 1);
            quickSort(arr, p + 1, high);
        }
    }

    static int partition(int arr[], int low, int high) {
        int pivot = low;

        int i = low, j = high;
        while (i < j) {
            while (i <= high && arr[i] <= arr[pivot])
                i++;
            while (j >= low && arr[j] > arr[pivot])
                j--;
            if (i < j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[j];
        arr[j] = arr[pivot];
        arr[pivot] = temp;

        return j;
    }
}
