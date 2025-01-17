// link - https://www.geeksforgeeks.org/problems/selection-sort/1

package GFG.Basics;

import java.util.Arrays;

public class Selection_Sort {
    public static void main(String[] args) {
        int[] arr = { 4, 1, 3, 9, 7 };
        selectionSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    public static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int min = i;
            for (int j = i; j < arr.length; j++) {
                if (arr[min] > arr[j])
                    min = j;
            }
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
}
