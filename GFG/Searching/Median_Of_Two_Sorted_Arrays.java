package GFG.Searching;

// Question - Given two sorted arrays of sizes N and M respectively. The task is to find the median of the two arrays
//            when they get merged.
//            If there are even number of elements in the resulting array, find the floor of the average of two medians.

// Input - int[] arr, brr
//       - int n = arr.length, m = brr.length

// Output - int
//        - return the median element (middle element) of the combined array if the combined array is of odd length
//        - else return the average of both middle elements if the length is even
//          eg. (2 + 3) / 2 = 2.5 but we have to return int so return 2

// Constraints - all values are within int range
//             - all values are >= 1 (which means no positives or zero)

class Solution {
    public static void main(String[] args) {
        int[] arr = { 1, 2 }, brr = { 3, 4 };
        // int n = arr.length, m = brr.length;
        // int[] arr = new int[100000];
        // int[] brr = new int[100000];

        // for (int i = 0; i < 100000; i++) {
        // arr[i] = i * 2; // Even numbers
        // brr[i] = i * 2 + 1; // Odd numbers
        // }

        long start = System.currentTimeMillis();
        System.out.println("Start time: " + start);
        System.out.println(findMedian(arr, arr.length, brr, brr.length));
        long end = System.currentTimeMillis();
        System.out.println("End time: " + end);
        System.out.println("Elapsed: " + (end - start));
    }

    public static int findMedian(int arr[], int n, int brr[], int m) {
        if (arr.length > brr.length) {
            int[] temp = arr;
            arr = brr;
            brr = temp;

            int t = n;
            n = m;
            m = t;
        }

        int nm = n + m;
        int half = nm / 2;

        int l = 0, r = n - 1;
        while (true) {
            // We need to do floor division here otherwise if we get something like -1 / 2
            // it would result to to 0 normally and we would be stuck in an infinite loop
            int mid = Math.floorDiv(l + r, 2);
            int otherMid = half - mid - 2;

            int arrLeft = mid >= 0 ? arr[mid] : Integer.MIN_VALUE;
            int arrRight = mid + 1 < n ? arr[mid + 1] : Integer.MAX_VALUE;
            int brrLeft = otherMid >= 0 ? brr[otherMid] : Integer.MIN_VALUE;
            int brrRight = otherMid + 1 < m ? brr[otherMid + 1] : Integer.MAX_VALUE;

            if (arrLeft <= brrRight && brrLeft <= arrRight) {
                if ((nm & 1) == 1) {
                    return Math.min(arrRight, brrRight);
                } else {
                    return (Math.max(arrLeft, brrLeft) + Math.min(arrRight, brrRight)) / 2;
                }
            } else if (arrLeft > brrRight) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
    }
}