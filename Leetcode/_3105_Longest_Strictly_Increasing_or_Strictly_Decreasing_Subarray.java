// link - https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

public class _3105_Longest_Strictly_Increasing_or_Strictly_Decreasing_Subarray {
    public int longestMonotonicSubarray(int[] nums) {
        int inc = 1, max = 1, dec = 1;

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                dec = 1;
                inc++;
                max = Math.max(max, inc);
            } else if (nums[i] < nums[i + 1]) {
                inc = 1;
                dec++;
                max = Math.max(max, dec);
            } else {
                inc = 1;
                dec = 1;
            }
        }

        return max;
    }
}
