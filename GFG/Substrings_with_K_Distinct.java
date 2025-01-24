// link - https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1

package GFG;

import java.util.HashSet;

public class Substrings_with_K_Distinct {
    public static void main(String[] args) {
        String s = "aba"; // ans = 3
        int k = 2;

        String s2 = "abaaca"; // ans = 7
        int k2 = 1;

        String s3 = "cdad"; // ans = 0
        int k3 = 4;

        System.out.println(countSubstr(s, k));
        System.out.println(countSubstr(s2, k2));
        System.out.println(countSubstr(s3, k3));
    }

    public static int countSubstr(String s, int k) {
        // we will use an array as a hashmap since we know the max size of input
        int[] letters = new int[26];
        int total = 0;

        // using 3 pointer approach
        // we need to consider the maximum possible subarray that satisfies the
        // condition as well as any array in between that thats why we'll use
        // the three pointer approach

        // n = near pointer (left near)
        // f = far pointer (left far)
        // i = right pointer
        int n = 0, f = 0;
        for (int i = 0; i < s.length(); i++) {
            if (++letters[(int) s.charAt(i) - 97] == 1)
                k--;

            // we have more than k elements in the letters hashmap
            while (k < 0) {
                // start removing elements starting from near pointer
                if (--letters[(int) s.charAt(n) - 97] == 0)
                    k++;
                n++;
                f = n;
            }

            // we have k number of distince elements but there are duplicates
            // within the window, so move the window forward until we find the
            // smallest sized window that still has k distince elements
            while (letters[(int)s.charAt(n) - 97] > 1) {
                letters[(int)s.charAt(n) - 97]--;
                n++;
            }

            // increment total if we have exactly k distince elements
            if (k == 0) {
                total += n - f + 1;
            }
        }

        return total;
    }

    // Naive solution- !Exceeds Time Limit so it may not be correct loginc wise
    // either! - Time = O(n^2) - Space = O(n)
    int countSubstrSlow(String s, int k) {
        int total = 0;
        HashSet<Character> set = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            int j = i;
            while (j < s.length() && set.size() <= k) {
                set.add(s.charAt(j));
                if (set.size() == k)
                    total++;
                j++;
            }
            set.clear();
        }
        return total;
    }
}
