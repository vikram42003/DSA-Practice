// link - https://leetcode.com/problems/longest-palindromic-substring/

public class _5_Longest_Palindromic_Substring {

    // Expand Around Center approach - Time = O(n^2) - Space = O(1)
    public String longestPalindromeEAC(String s) {
        if (s.length() <= 1)
            return s;

        int[] max = { 0, 1 };
        for (int i = 0; i < s.length(); i++) {
            int[] even = isPalindromeEAC(s, i, i);
            int[] odd = isPalindromeEAC(s, i, i + 1);

            if (even[1] - even[0] > max[1] - max[0]) {
                max = even;
            }
            if (odd[1] - odd[0] > max[1] - max[0]) {
                max = odd;
            }
        }

        return s.substring(max[0], max[1]);
    }

    public int[] isPalindromeEAC(String s, int l, int r) {
        while (l >= 0 && r < s.length() && (s.charAt(l) == s.charAt(r))) {
            l--;
            r++;
        }
        return new int[] { l + 1, r };
    }

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
            if (s.charAt(l) != s.charAt(r))
                return false;
            l++;
            r--;
        }
        return true;
    }
}
