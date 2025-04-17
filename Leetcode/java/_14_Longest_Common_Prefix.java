// link - https://leetcode.com/problems/longest-common-prefix/

import java.util.Arrays;

public class _14_Longest_Common_Prefix {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String first = strs[0];
        String last = strs[strs.length - 1];

        int i = 0;
        while (i < first.length() && i < last.length()) {
            if (first.charAt(i) == last.charAt(i))
                i++;
            else
                break;
        }
        return first.substring(0, i);
    }
}
