// link - https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557

import java.util.ArrayList;

public class Painters_Partition_Problem {
    public static int findLargestMinDistance(ArrayList<Integer> boards, int k) {
        int l = 0, r = 0;
        for (int num : boards) {
            l = Math.max(l, num);
            r += num;
        }

        while (l < r) {
            int mid = l + ((r - l) / 2);
            if (check(mid, boards, k)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }

    public static boolean check(int mid, ArrayList<Integer> boards, int k) {
        int curr = 0;
        for (int num : boards) {
            curr += num;
            if (curr > mid) {
                curr = num;
                k--;
            }
        }
        k--;
        return k >= 0;
    }
}
