// link - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/ 

import java.util.Arrays;

public class Capacity_To_Ship_Packages_Within_D_Days_1011 {
    public static void main(String[] args) {
        // int[] weights = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }; // ans = 15
        // int days = 5;

        int[] weights2 = { 1, 2, 3, 1, 1 }; // ans = 3
        int days2 = 4;

        // System.out.println(shipWithinDays(weights, days));
        System.out.println(shipWithinDays(weights2, days2));
    }

    public static int shipWithinDays(int[] weights, int days) {
        int l = 0, r = 0;
        for (int num : weights) {
            l = Math.max(l, num);
            r += num;
        }

        while (l < r) {
            int mid = l + ((r - l) / 2);

            if (canWeShipThis(mid, weights, days)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }

    public static boolean canWeShipThis(int mid, int[] weights, int days) {
        int curr = 0;
        for (int num : weights) {
            if (num > mid)
                return false;
            curr += num;
            if (curr > mid) {
                curr = num;
                days--;
            }
        }
        if (curr > 0)
            days--;
        return days >= 0;
    }
}
