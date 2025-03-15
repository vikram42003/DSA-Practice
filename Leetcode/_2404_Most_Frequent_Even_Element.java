// link - https://leetcode.com/problems/most-frequent-even-element/

import java.util.HashMap;

public class _2404_Most_Frequent_Even_Element {
    // Naive Solution
    public int mostFrequentEven(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i : nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        int max = 0;
        int ans = Integer.MAX_VALUE;
        for (int key : map.keySet()) {
            if ((key & 1) == 0) {
                int count = map.get(key);
                if (count == max) {
                    ans = Math.min(ans, key);
                } else if (count > max) {
                    ans = key;
                    max = count;
                }
            }
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
