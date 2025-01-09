// link - https://www.naukri.com/code360/problems/aggressive-cows_1082559

import java.util.Arrays;

public class Agressive_Cows {
    public static void main(String[] args) {
        // int[] stalls = { 1, 2, 3 }; // k = 2   ans = 2
        int[] stalls2 = { 87, 93, 51, 81, 68, 99, 59 }; // k = 4   ans = 13

        System.out.println(aggressiveCows(stalls2, 4));
    }

    public static int aggressiveCows(int []stalls, int k) {
        Arrays.sort(stalls);

        int l = 0, r = stalls[stalls.length - 1] - stalls[0];
        while (l <= r) {
            int mid = l + ((r - l) / 2);

            if (check(stalls, mid, k)) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return r;
    }

    public static boolean check(int[] stalls, int dist, int cows) {
        // first cow will be place at index 0 so do cows-- at the start
        cows--;
        
        int current = 0;
        for (int i = 0; i < stalls.length - 1; i++) {
            current += stalls[i + 1] - stalls[i];
            if (current >= dist) {
                current = 0;
                cows--;
            }
            if (cows == 0) {
                return true;
            }
        }

        return false;
    }
}
