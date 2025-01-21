// link - https://leetcode.com/problems/string-to-integer-atoi/

public class _8_String_to_Integer_atoi {
    public int myAtoi(String s) {
        s = s.trim();
        if (s.length() == 0)
            return 0;
        long num = 0;
        boolean negative = s.charAt(0) == '-';
        int i = negative ? 1 : 0;
        if (s.charAt(0) == '+')
            i++;

        while (i < s.length() && s.charAt(i) >= '0' && s.charAt(i) <= '9') {
            if (num >= Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            } else if (num <= Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }

            num *= 10;

            if (negative == true) {
                num -= s.charAt(i) - '0';
            } else {
                num += s.charAt(i) - '0';
            }
            i++;
        }

        if (num >= Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        } else if (num <= Integer.MIN_VALUE) {
            return Integer.MIN_VALUE;
        } else {
            return (int) num;
        }
    }
}
