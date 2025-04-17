//  link - https://leetcode.com/problems/largest-odd-number-in-string/

public class _1903_Largest_Odd_Number_in_String {
    public String largestOddNumber(String num) {
        int i = num.length() - 1;
        while (i >= 0) {
            if (((num.charAt(i) - '0') & 1) == 1)
                return num.substring(0, i + 1);
            i--;
        }
        return "";
    }
}
