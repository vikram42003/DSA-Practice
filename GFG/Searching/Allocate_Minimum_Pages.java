package GFG.Searching;

public class Allocate_Minimum_Pages {
    public static void main(String[] args) {
        int[] arr = { 12, 34, 67, 90 }; // ans = 113
        int k = 2;

        System.out.println(findPages(arr, k));
    }

    public static int findPages(int[] arr, int k) {
        // Edge case 1 - k is greater than array size
        if (k > arr.length)
            return -1;

        // Edge case 2 - array length is 1
        if (arr.length == 1)
            return arr[0];

        int totalSum = 0;
        int max = 0;
        for (int i = 0; i < arr.length; i++) {
            totalSum += arr[i];
            max = Math.max(max, arr[i]);
        }

        // Edge case 3 - if k is 1
        if (k == 1)
            return totalSum;

        int ans = 0;
        int l = max, r = totalSum;
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            if (checkIfCorrect(arr, mid, k)) {
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return ans;
    }

    // check feasibility of solution using greedy partitioning
    public static boolean checkIfCorrect(int[] arr, int mid, int k) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];

            if (sum > mid) {
                sum = arr[i];
                k--;
            }

            if (k <= 0) {
                return false;
            }
        }

        return true;
    }
}
