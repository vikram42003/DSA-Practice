// link - https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

public class _1781_Sum_of_Beauty_of_All_Substrings {
    public int beautySum(String s) {
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            char[] c = new char[26];
            for (int j = i; j < s.length(); j++) {
                c[s.charAt(j) - 'a']++;

                int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
                for (int k = 0; k < 26; k++) {
                    if (c[k] == 0)
                        continue;
                    max = Math.max(max, c[k]);
                    min = Math.min(min, c[k]);
                }

                count += max - min;
            }
        }

        return count;
    }
}
