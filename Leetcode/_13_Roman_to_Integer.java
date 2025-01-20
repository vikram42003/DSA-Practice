// link - https://leetcode.com/problems/roman-to-integer/

public class _13_Roman_to_Integer {
    public int romanToInt(String s) {
        int sum = 0;
        char prev = 'z';
        for (char c : s.toCharArray()) {
            if (prev == 'I' && (c == 'V' || c == 'X')) {
                sum -= 2;
            } else if (prev == 'X' && (c == 'L' || c == 'C')) {
                sum -= 20;
            } else if (prev == 'C' && (c == 'D' || c == 'M')) {
                sum -= 200;
            }

            switch (c) {
                case 'I':
                    sum += 1;
                    break;
                case 'V':
                    sum += 5;
                    break;
                case 'X':
                    sum += 10;
                    break;
                case 'L':
                    sum += 50;
                    break;
                case 'C':
                    sum += 100;
                    break;
                case 'D':
                    sum += 500;
                    break;
                case 'M':
                    sum += 1000;
                    break;
            }
            prev = c;
        }
        return sum;
    }
}
