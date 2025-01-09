class _852_Peak_Index_in_a_Mountain_Array {
    public int peakIndexInMountainArray(int[] arr) {
        int peak = 0, l = 0, r = arr.length - 1;

        while (l <= r) {
            int mid = l + ((r - l) / 2);
            int next = mid < arr.length - 1 ? arr[mid + 1] : -1;

            peak = arr[mid] > arr[peak] ? mid : peak;

            if (arr[mid] > next) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return peak;
    }
}