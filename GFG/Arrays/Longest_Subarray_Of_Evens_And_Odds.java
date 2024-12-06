class Solution {
    // arr[]: input array
    // n: size of array
    // Function to find the length of longest subarray of even and odd numbers.
    public static int maxEvenOdd(int arr[], int n) {
        // your code here
        int longest = 1, curr = 1;

        for (int i = 0; i < n - 1; i++) {
            // first even second odd case
            if ((arr[i] & 1) == 0 && (arr[i + 1] & 1) == 1) {
                curr++;
                if (curr > longest)
                    longest = curr;
                // first odd second even case
            } else if ((arr[i] & 1) == 1 && (arr[i + 1] & 1) == 0) {
                curr++;
                if (curr > longest)
                    longest = curr;
                // first and second both even or odd case
            } else {
                curr = 1;
            }
        }

        return longest;
    }
}