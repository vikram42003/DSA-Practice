// link - https://www.naukri.com/code360/problems/allocate-books_1090540

import java.util.ArrayList;

class Allocate_Books {
    public static int findPages(ArrayList<Integer> arr, int n, int m) {
        if (m > n)
            return -1;
        int l = 0, r = 0;
        for (int num : arr) {
            l = Math.max(l, num);
            r += num;
        }

        while (l < r) {
            int mid = l + ((r - l) / 2);

            if (check(mid, arr, m)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }

    public static boolean check(int mid, ArrayList<Integer> arr, int m) {
        int curr = 0;
        for (int pages : arr) {
            curr += pages;
            if (curr > mid) {
                curr = pages;
                m--;
            }
        }
        // do another m-- to account for the last book leftover
        // after the loop ends
        m--;
        return m >= 0;
    }
}