public class _4_Median_of_Two_Sorted_Arrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] arr = nums1, brr = nums2;
        int n = arr.length, m = brr.length;
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
                    return (double) (Math.max(arrLeft, brrLeft) + Math.min(arrRight, brrRight)) / 2;
                }
            } else if (arrLeft > brrRight) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
    }
}
