// link - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

// make a hashmap
// iterate over the array
// put values in the hashmap and track the size
// lets say k = 3
// if size < 3
//     then just add the values
// if size >= 3 and map.size() = 3 then that means we have 3 distinct numbers
//     so track the max and shorten the window
// if size >= 3 but map.size() < 3 then that means we have duplicate(s)
//     so shorten the window one at a time

import java.util.HashMap;

public class _2461_Maximum_Sum_of_Distinct_Subarrays_With_Length_K {
    public long maximumSubarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();

        long max = Integer.MIN_VALUE;
        long curr = 0;
        int size = 0;

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
            size++;
            curr += (long) nums[i];

            if (size == k) {
                if (map.size() == k) {
                    max = Math.max(max, curr);
                }

                size--;
                curr -= (long) nums[i - (k - 1)];
                map.put(nums[i - (k - 1)], map.get(nums[i - (k - 1)]) - 1);
                if (map.get(nums[i - (k - 1)]) <= 0) {
                    map.remove(nums[i - (k - 1)]);
                }
            }
        }

        return max == Integer.MIN_VALUE ? 0 : max;
    }
}
