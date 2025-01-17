// link - https://www.geeksforgeeks.org/problems/insertion-sort/0

package GFG.Basics;

public class Insertion_Sort {
    public void insertionSort(int arr[]) {
        for (int i = 1; i < arr.length; i++) {
            int j = i;
            while (j > 0 && arr[j] < arr[j - 1]) {
                int temp = arr[j];
                arr[j] = arr[j - 1];
                arr[j - 1] = temp;
                j--;
            }
        }
    }
}
