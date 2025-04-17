// link - https://leetcode.com/problems/valid-palindrome/

class _125_Valid_Palindrome {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            char a = Character.toLowerCase(s.charAt(l));
            if (!((a >= 97 && a <= 122) || (a >= '0' && a <= '9'))) {
                l++;
                continue;
            }

            char b = Character.toLowerCase(s.charAt(r));
            if (!((b >= 97 && b <= 122) || (b >= '0' && b <= '9'))) {
                r--;
                continue;
            }

            if (a != b) {
                return false;
            }

            l++;
            r--;
        }
        return true;
    }
}