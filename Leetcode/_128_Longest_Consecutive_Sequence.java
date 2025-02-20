// link - https://leetcode.com/problems/longest-consecutive-sequence/

import java.util.HashSet;

public class _128_Longest_Consecutive_Sequence {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums)
            set.add(num);

        int max = 0;
        for (int i : set) {
            if (!set.contains(i - 1)) {
                int count = 0;
                while (set.contains(i + count)) {
                    count++;
                }
                max = Math.max(max, count);
            }
        }

        return max;
    }
}
