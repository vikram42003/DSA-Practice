// link - https://leetcode.com/problems/smallest-number-with-all-set-bits/

public class _3370_Smallest_Number_With_All_Set_Bits {
    public int smallestNumber(int n) {
        int num = 0;
        while (num < n) {
            num <<= 1;
            num = num | 1;
        }
        return num;
    }
}
