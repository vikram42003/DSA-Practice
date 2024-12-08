class Solution {

    public int peakElement(int[] arr) {
        // If theres only 1 element
        if (arr.length == 1)
            return 0;
        // If first element is peak
        if (arr[0] > arr[1])
            return 0;
        // If last element is peak
        if (arr[arr.length - 1] > arr[arr.length - 2])
            return arr.length - 1;

        int l = 1, r = arr.length - 2;
        while (l <= r) {
            int mid = l + ((r - l) / 2);

            if (arr[mid - 1] < arr[mid] && arr[mid + 1] < arr[mid]) {
                return mid;
            } else if (arr[mid - 1] > arr[mid]) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return -1;
    }
}