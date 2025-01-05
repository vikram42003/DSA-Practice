package GFG.Searching;

class Count_1s_In_Binary_Array {
    // Function to count number of ones in the binary array
    // N: size of array
    // arr[]: input array
    public static int countOnes(int arr[], int N) {
        int l = 0, r = N - 1;
        int toSearch = 1, rightMost = -1;

        while (l <= r) {
            int mid = l + ((r - l) / 2);
            if (arr[mid] == toSearch) {
                if (rightMost == -1 || mid > rightMost)
                    rightMost = mid;
                l = mid + 1;
            } else if (arr[mid] > toSearch) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return rightMost + 1;
    }
}