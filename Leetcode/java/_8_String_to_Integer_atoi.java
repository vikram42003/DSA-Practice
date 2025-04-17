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

    // Faster
    public int myAtoiFaster(String s) {
        if (s.length() == 0)
            return 0;

        int i = 0;
        int sign = 1;

        while (i < s.length() && s.charAt(i) == ' ') {
            i++;
        }

        if (i >= s.length())
            return 0;

        if (s.charAt(i) == '-') {
            i++;
            sign = -1;
        } else if (s.charAt(i) == '+') {
            i++;
        }

        int sum = 0;
        while (i < s.length() && (s.charAt(i) >= '0' && s.charAt(i) <= '9')) {
            if (sum > Integer.MAX_VALUE / 10) {
                if (sign == 1) {
                    return Integer.MAX_VALUE;
                } else {
                    return Integer.MIN_VALUE;
                }
            }
            sum *= 10;

            if (sum > Integer.MAX_VALUE - (s.charAt(i) - '0')) {
                if (sign == 1) {
                    return Integer.MAX_VALUE;
                } else {
                    return Integer.MIN_VALUE;
                }
            }
            sum += s.charAt(i) - '0';

            i++;
        }

        return sum * sign;
    }
}
