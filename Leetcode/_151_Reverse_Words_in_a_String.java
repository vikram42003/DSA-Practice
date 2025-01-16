// link - https://leetcode.com/problems/reverse-words-in-a-string/description/

// JS solution - Did this cause i was bored, js is kinda neat tho ngl
// var reverseWords = function(s) {
//     return s.trim().split(" ").filter(s => s !== "").reverse().join(" ");
// };

import java.util.Arrays;

public class _151_Reverse_Words_in_a_String {
    public static void main(String[] args) {
        String s = "another good   example    here";

        System.out.println(reverseWords(s));
    }

    public static String reverseWords(String s) {
        s = s.trim();
        char[] c = s.toCharArray();

        c = removeExtraSpaces(c);
        reverse(c, 0, c.length - 1);
        reverseEachWord(c);

        return new String(c);
    }

    // a.good...example....here

    public static char[] removeExtraSpaces(char[] c) {
        int i = 1, j = 1;
        while (j < c.length) {
            if (c[i] == ' ' && c[i - 1] == ' ') {
                while (j < c.length && c[j] == ' ') {
                    j++;
                }
                while (j < c.length && c[j] != ' ') {
                    char temp = c[i];
                    c[i] = c[j];
                    c[j] = temp;
                    i++;
                    j++;
                }

                if (j == c.length) {
                    break;
                }

                j = i;
            }
            i++;
            j++;
        }

        return Arrays.copyOfRange(c, 0, i);
    }

    public static void reverse(char[] c, int l, int r) {
        while (l < r) {
            char temp = c[l];
            c[l] = c[r];
            c[r] = temp;
            l++;
            r--;
        }
    }

    public static void reverseEachWord(char[] c) {
        int i = 0;
        for (int j = 0; j < c.length; j++) {
            if (c[j] == ' ') {
                reverse(c, i, j - 1);
                i = j + 1;
            }
        }
        reverse(c, i, c.length - 1);
    }
}
