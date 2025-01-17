// link - https://www.geeksforgeeks.org/problems/bubble-sort/1

package GFG.Basics;

public class Bubble_Sort {
    public static void bubbleSort(int arr[]) {
        for (int i = arr.length; i > 0; i--) {
            int didWeSwap = 0;
            for (int j = 0; j < i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    didWeSwap = 1;
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
            if (didWeSwap == 0)
                return;
        }
    }

    public static void recursiveBubbleSort(int[] arr, int n) {
        if (n == 1)
            return;

        for (int i = 1; i < n; i++) {
            if (arr[i - 1] > arr[i]) {
                int temp = arr[i];
                arr[i] = arr[i - 1];
                arr[i - 1] = temp;
            }
        }

        recursiveBubbleSort(arr, n - 1);
    }
}
