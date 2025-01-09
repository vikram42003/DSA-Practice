// link - https://www.naukri.com/code360/problems/implement-upper-bound_8165383

public class Implement_Upper_Bound {
    public static int upperBound(int[] arr, int x, int n) {
        if (arr[n - 1] <= x)
            return n;

        int l = 0, r = n - 1;

        while (l < r) {
            int mid = l + ((r - l) / 2);

            if (arr[mid] > x) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return r;
    }
}
