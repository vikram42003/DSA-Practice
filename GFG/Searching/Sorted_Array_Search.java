class Sorted_Array_Search {
    static boolean searchInSorted(int arr[], int k) {
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