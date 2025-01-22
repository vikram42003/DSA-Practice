// link - https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1

package GFG;

import java.util.HashSet;

public class Substrings_with_K_Distinct {
    // Naive solution- !Exceeds Time Limit so it may not be correct loginc wise either! - Time = O(n^2) - Space = O(n)
    int countSubstr(String s, int k) {
        int total = 0;
        HashSet<Character> set = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            int j = i;
            while (j < s.length() && set.size() <= k) {
                set.add(s.charAt(j));
                if (set.size() == k) total++;
                j++;
            }
            set.clear();
        }
        return total;
    }
}
