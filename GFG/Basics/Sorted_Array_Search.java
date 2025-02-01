// link - https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1

package GFG.Basics;

public class Sorted_Array_Search {
    static boolean searchInSorted(int arr[], int k) {
        // Your code here
        int l = 0, r = arr.length - 1;

        while (l <= r) {
            int mid = l + ((r - l) / 2);
            if (arr[mid] == k) {
                return true;
            } else if (arr[mid] > k) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return false;
    }
}
