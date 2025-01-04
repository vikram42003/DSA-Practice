// link - https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1?

package GFG.Searching;

public class Number_Of_Occurence {
    int countFreq(int[] arr, int target) {
        int left = binarySearchLeft(arr, target);
        int right = binarySearchRight(arr, target);

        if (left == -1 && right == -1) {
            return 0;
        } else if (left == right) {
            return 1;
        } else {
            return right - left + 1;
        }
    }

    int binarySearchLeft(int[] arr, int x) {
        int l = 0, r = arr.length - 1;
        while (l < r) {
            int mid = l + ((r - l) / 2);
            if (arr[mid] == x) {
                r = mid;
            } else if (arr[mid] < x) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return r >= 0 && arr[r] == x ? r : -1;
    }

    int binarySearchRight(int[] arr, int x) {
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            if (arr[mid] == x) {
                l = mid + 1;
            } else if (arr[mid] < x) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return r >= 0 && arr[r] == x ? r : -1;
    }
}
