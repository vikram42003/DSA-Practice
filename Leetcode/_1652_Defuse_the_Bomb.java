// link - https://leetcode.com/problems/defuse-the-bomb/

import java.util.Arrays;

public class _1652_Defuse_the_Bomb {
    public static void main(String[] args) {
        int[] code = { 5, 7, 1, 4 };
        int k = 3; // ans = [12, 10, 16, 13]
        int k2 = 0; // ans = [0, 0, 0, 0]
        int k3 = -2; // ans = [5, 9, 12, 8]

        System.out.println(Arrays.toString(decrypt(code, k3)));
    }

    // linear time and space approach - Time = O(n) - Space = O(n)
    public static int[] decrypt(int[] code, int k) {
        if (k > 0) {
            code = sumNextK(code, k);
        } else if (k < 0) {
            code = sumPrevK(code, k);
        } else {
            setAllZero(code);
        }
        return code;
    }

    public static int[] sumNextK(int[] code, int k) {
        int[] temp = new int[code.length];
        int sum = 0;

        for (int i = 0; i < k; i++) {
            sum += code[i];
        }

        for (int i = 0; i < temp.length; i++) {
            sum -= code[i];
            sum += code[(i + k) % code.length];
            temp[i] = sum;
        }

        return temp;
    }

    public static int[] sumPrevK(int[] code, int k) {
        int[] temp = new int[code.length];
        int sum = 0;

        // turn k positive
        k *= -1;

        for (int i = code.length - k; i < code.length; i++) {
            sum += code[i];
        }

        for (int i = 0; i < code.length; i++) {
            temp[i] = sum;
            sum -= code[((code.length - k) + i) % code.length];
            sum += code[i];
        }

        return temp;
    }

    public static void setAllZero(int[] code) {
        for (int i = 0; i < code.length; i++) {
            code[i] = 0;
        }
    }

    // Optimal Approach - Time = O(n) - Space = O(1) - Did not work
    // Also, it might be impossible, couldnt get sumPrevK to work in O(1) space
    public static int[] optimalDecrypt(int[] code, int k) {
        if (k > 0) {
            optimalSumNextK(code, k);
        } else if (k < 0) {
            optimalSumPrevK(code, k);
        } else {
            optimalSetAllZero(code);
        }
        return code;
    }

    public static void optimalSumNextK(int[] code, int k) {
        int r = 0;
        int window = 0;
        while (r < k) {
            window += code[r];
            r++;
        }

        int toAddNext = code[r % code.length];
        for (int i = 0; i < code.length; i++) {
            window -= code[i];
            window += toAddNext;
            r++;
            toAddNext = code[r % code.length];
            code[i] = window;
        }
    }

    public static void optimalSumPrevK(int[] code, int k) {
        int l = code.length - 1;
        int window = 0;
        for (int i = 0; i > k; i--) {
            window += code[l];
            l--;
        }

        l++;
        int prevVal = 0;
        for (int i = 0; i < code.length; i++) {
            prevVal = code[i];
            code[i] = window;
            window -= code[l % code.length];
            window += prevVal;
            l++;
        }
    }

    public static void optimalSetAllZero(int[] code) {
        for (int i = 0; i < code.length; i++) {
            code[i] = 0;
        }
    }
}
