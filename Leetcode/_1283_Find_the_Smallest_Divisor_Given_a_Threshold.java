// link - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

public class _1283_Find_the_Smallest_Divisor_Given_a_Threshold {
    public int smallestDivisor(int[] nums, int threshold) {
        int l = 1, r = (int) 1e6;

        while (l < r) {
            int mid = l + ((r - l) / 2);
            if (check(mid, nums, threshold)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }

    public boolean check(int mid, int[] nums, int threshold) {
        int total = 0;
        for (int num : nums) {
            total += num / mid;
            total += num % mid == 0 ? 0 : 1;
        }
        return total <= threshold;
    }
}
