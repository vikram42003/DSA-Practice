// link - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

public class _1482_Minimum_Number_of_Days_to_Make_m_Bouquets {
    public int minDays(int[] bloomDay, int m, int k) {
        if (m * k > bloomDay.length || m * k < 0)
            return -1;

        int l = 1, r = (int) 1e9;

        while (l < r) {
            int mid = l + ((r - l) / 2);
            if (canWeMakeBouquets(mid, bloomDay, m, k)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }

    public boolean canWeMakeBouquets(int mid, int[] bloomDay, int m, int k) {
        int total = 0, curr = 0;
        for (int num : bloomDay) {
            if (num <= mid) {
                curr++;
            } else {
                curr = 0;
            }
            if (curr >= k) {
                total++;
                curr = 0;
            }
        }
        return total >= m;
    }
}
