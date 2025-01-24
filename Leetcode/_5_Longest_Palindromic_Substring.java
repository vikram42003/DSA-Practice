// link - https://leetcode.com/problems/longest-palindromic-substring/

public class _5_Longest_Palindromic_Substring {


    // Naive Solution - Time = O(n^3) - Space = O(1)
    public String longestPalindrome(String s) {
        int max = 0;
        int ansStart = 0, ansEnd = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j < s.length(); j++) {
                if (isPalindrome(s, i, j)) {
                    if (j - i > max) {
                        max = j - i;
                        ansStart = i;
                        ansEnd = j;
                    }
                }
            }
        }
        return s.substring(ansStart, ansEnd + 1);
    }

    public boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++; r--;
        }
        return true;
    }
}
