// link - https://leetcode.com/problems/longest-substring-without-repeating-characters/

import java.util.HashSet;

public class _3_Longest_Substring_Without_Repeating_Characters {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int max = 0, curr = 0;
        int i = 0, j = 0;

        while (j < s.length()) {
            if (!set.contains(s.charAt(j))) {
                curr++;
                max = Math.max(max, curr);
                set.add(s.charAt(j));
                j++;
            } else {
                while (set.contains(s.charAt(j))) {
                    set.remove(s.charAt(i));
                    i++;
                    curr--;
                }
            }
        }

        return max;
    }
}
