// link - https://leetcode.com/problems/3sum/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class _15_3Sum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            // Ensure that we skip any duplicates
            // We have sorted nums, so if, after sorting, nums is [ -1, -1, 0, 1 ]
            // Then any combination that starts with nums[0] (which is -1) will be the same
            // as any
            // combination that starts with nums[1] (which is also -1)
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            // Solve the rest of the problem like its a 2sum with sorted array
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];

                if (sum > 0) {
                    r--;
                } else if (sum < 0) {
                    l++;
                } else {
                    List<Integer> list = new ArrayList<>();
                    list.add(nums[i]);
                    list.add(nums[l]);
                    list.add(nums[r]);
                    ans.add(list);
                    // Move l pointer to see if theres any other valid combination with the current
                    // starting point
                    // We only move the l pointer to a non-duplicate position because this if-else
                    // if-else condition that we have here will automatically move the r pointer to
                    // a non-duplicate index
                    l++;
                    while (l < r && nums[l] == nums[l - 1])
                        l++;
                }
            }
        }

        return ans;
    }
}
