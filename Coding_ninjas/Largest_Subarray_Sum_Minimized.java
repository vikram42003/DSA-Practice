package Coding_ninjas;
// link - https://www.naukri.com/code360/problems/largest-subarray-sum-minimized_7461751

class Largest_Subarray_Sum_Minimized {
    public static int largestSubarraySumMinimized(int[] a, int k) {
        if (a.length < k)
            return -1;

        int l = 0, r = 0;
        for (int num : a) {
            l = Math.max(l, num);
            r += num;
        }

        while (l < r) {
            int mid = l + ((r - l) / 2);
            if (check(mid, a, k)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }

    public static boolean check(int mid, int[] a, int k) {
        k--;
        long curr = 0;
        for (int num : a) {
            curr += num;
            if (curr > mid) {
                curr = num;
                k--;
            }
        }
        return k >= 0;
    }
}