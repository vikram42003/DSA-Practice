// link - https://www.naukri.com/code360/problems/nth-root-of-m_1062679

package Misc.coding_ninjas;

public class Find_Nth_Root_Of_M {
    public static int NthRoot(int n, int m) {
        int l = 1, r = m;
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            long num = fastExponent(mid, n);
            if (num == m) {
                return mid;
            } else if (num > m || num == Long.MAX_VALUE) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return -1;
    }

    public static long fastExponent(int num, int e) {
        if (e == 0) {
            return 1;
        } else if (e == 1) {
            return num;
        } else {
            long res = fastExponent(num, e / 2);
            if (res > Integer.MAX_VALUE)
                return Long.MAX_VALUE;

            if ((e & 1) == 0) {
                long result = res * res;
                if (result > Integer.MAX_VALUE)
                    return Long.MAX_VALUE;
                return result;
            } else {
                long result = res * num * res;
                if (result > Integer.MAX_VALUE)
                    return Long.MAX_VALUE;
                return result;
            }
        }
    }
}
