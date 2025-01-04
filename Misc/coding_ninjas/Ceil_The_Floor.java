// link - https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401

package Misc.coding_ninjas;

public class Ceil_The_Floor {
    public static int[] getFloorAndCeil(int[] a, int n, int x) {
        int floor = floor(a, x);
        int ceil = ceil(a, x);
        return new int[] { floor, ceil };
    }

    public static int floor(int[] arr, int x) {
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            if (arr[mid] <= x) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return (r >= 0) && (arr[r] <= x) ? arr[r] : -1;
    }

    public static int ceil(int[] arr, int x) {
        int l = 0, r = arr.length - 1;
        while (l < r) {
            int mid = l + ((r - l) / 2);
            if (arr[mid] >= x) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return (r <= arr.length - 1) && (arr[r] >= x) ? arr[r] : -1;
    }
}
