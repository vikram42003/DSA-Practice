// link - https://leetcode.com/problems/maximum-ascending-subarray-sum/

public class _1800_Maximum_Ascending_Subarray_Sum {
    public int maxAscendingSum(int[] nums) {
        int max = nums[0];
        int curr = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] < nums[i]) {
                curr += nums[i];
                max = Math.max(max, curr);
            } else {
                max = Math.max(max, curr);
                curr = nums[i];
            }
        }

        return max;
    }
}
