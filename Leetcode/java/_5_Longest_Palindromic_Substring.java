// link - https://leetcode.com/problems/longest-palindromic-substring/

public class _5_Longest_Palindromic_Substring {
    public static void main(String[] args) {
        String s = "babad"; // ans = bab OR aba
        String s2 = "cbbd"; // ans = bb

        System.out.println(longestPalindromeManachers(s));
        System.out.println(longestPalindromeManachers(s2));
    }

    // Manacher's Algorithm - Time = O(n) - Space = O(n)

    // (The code for manachers is hella unoptimised, retry this and make it more optimized when you revisit this one)

    // put a unique string like "#" between the string so that we are technically
    // calculating
    // odd palindromes
    // iterate over each char
    // keep track of l and r denoting the left and right bounds of the current
    // substring
    // the idea is that the length of the substring to the left of the current
    // parent substring will be the same or greater for the sub palindromes to the
    // right
    // check if we have already calculated and assign the max possible value of the
    // palindrome
    // to the one at the right which will be min(r - l, (mid - (r - mid)))
    // thats becuase anything that is after r is unexplored sso we dont know if it
    // will make a
    // palindrome or not
    // so after that, we will manually check whether we can make a bigger palindrome
    // or not
    // and in each iteration we check whether current one is the biggest palindrome,
    // if yes then return that substring at the end
    // and thats it!

    // 0 1 2 3 4 5 6
    // m i r
    // m - (i - m) = 3 - (5 - 3) = 3 - 2 = 1

    // # 0 # 1 # 2 # 3 # 4 # 5 # 6 #

    public static String longestPalindromeManachers(String s) {
        if (s.length() <= 1) {
            return s;
        }

        // taking the separating character as "#" since the input is alphanumeric
        String str = s.replaceAll("", "#");

        int[] count = new int[str.length()];

        int maxSize = 0;
        int maxIdx = 0;

        // m is the middle of the current largest palindrome
        // r is the rightmost element of the current largest palindrome
        // we dont need an l variable because we can just calculate it
        // i is the current element we are checking
        int r = 0;
        int m = 0;
        for (int i = 0; i < str.length(); i++) {
            if (i < r) {
                count[i] = Math.min(r - i, count[2 * m - i]);
            }

            int a = i - count[i];
            int b = count[i] + i;
            while (a >= 0 && b < count.length && (str.charAt(a) == str.charAt(b))) {
                count[i]++;
                a--;
                b++;
            }

            if (b > r) {
                m = i;
                r = b - 1;
            }

            if (count[i] > maxSize) {
                maxSize = count[i];
                maxIdx = i;
            }
        }

        return str.substring(maxIdx - maxSize + 1, maxIdx + maxSize).replace("#", "");
    }

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
