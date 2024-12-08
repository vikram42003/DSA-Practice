class Solution {
    // Function to find the minimum element in sorted and rotated array.
    static int minNumber(int arr[], int low, int high) {
        int lowest = Integer.MAX_VALUE;

        while (low <= high) {
            int mid = low + ((high - low) / 2);
            lowest = Math.min(lowest, arr[mid]);
            lowest = Math.min(lowest, arr[low]);
            if (arr[low] <= arr[mid]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return lowest;
    }
}